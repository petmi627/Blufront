#!/usr/bin/python3
import ts3, sys, time

try:
    with ts3.query.TS3Connection("127.0.0.1", port=25639) as ts3conn:
        # Note, that the client will wait for the response and raise a
        # **TS3QueryError** if the error id of the response is not 0.
        try:
            ts3conn.auth(apikey="")
        except ts3.query.TS3QueryError as err:
            print("Login failed:", err.resp.error["msg"])
            exit(1)

        clid = ts3conn.whoami().parsed[0]["clid"]

        if len(sys.argv) > 1:
            if sys.argv[1] == "toogle_mute":
                if int(ts3conn.clientvariable(clid=clid, client_input_muted=None).parsed[0]['client_input_muted']) == 0:
                    ts3conn.clientupdate(client_input_muted=1)
                else:
                    ts3conn.clientupdate(client_input_muted=0)
            elif sys.argv[1] == "toogle_sound":
                if int(ts3conn.clientvariable(clid=clid, client_output_muted=None).parsed[0]['client_output_muted']) == 0:
                    ts3conn.clientupdate(client_output_muted=1)
                else:
                    ts3conn.clientupdate(client_output_muted=0)
            elif sys.argv[1] == "toogle_away":
                if int(ts3conn.clientvariable(clid=clid, client_away=None).parsed[0]['client_away']) == 0:
                    ts3conn.clientupdate(client_away=1)
                    if len(sys.argv) > 2:
                        ts3conn.clientupdate(client_away_message=sys.argv[2])
                else:
                    ts3conn.clientupdate(client_away=0)
        else:
            while True:
                try:
                    time.sleep(0.5)
                    ts3conn.channelconnectinfo()
                    cid = ts3conn.whoami().parsed[0]["cid"]
                    if int(ts3conn.clientvariable(clid=clid, client_output_muted=None).parsed[0]['client_output_muted']) == 1:
                        sys.stdout.write(" \n")
                    else:
                        resp = ts3conn.channelclientlist(cid=cid, voice=True)
                        speaking = []
                        for client in resp.parsed:
                            if int(client["client_flag_talking"]) > 0:
                                speaking.append(client['client_nickname'])
#                        if len(speaking) > 2:
#                            sys.stdout.write(" " + speaking[0] + ", " speaking[1] + " and " + str(len(speaking)-2) + " others" + "\n")
                        if len(speaking) > 0:
                            sys.stdout.write("  " + ", ".join(speaking) + "\n")
                        else:
                            sys.stdout.write(" \n")
                except BaseException as e:
                    time.sleep(1)
                    continue

    ts3conn.quit()
    ts3conn.close()
except BaseException as e:
    exit(1)
