#!/bin/bash
for i in $(playerctl -l);
do
	player_status=$(/usr/bin/playerctl -p "$i" status 2> /dev/null)
	if [[ $? -eq 0 ]]; then
	    case $player_status in
                Playing)
                        notify-send "pausing $(/usr/bin/playerctl -p "$i" metadata title)"
        	        /usr/bin/playerctl -p "$i" pause &
         	        ;;
                Paused)
                        notify-send "playing $(/usr/bin/playerctl -p "$i" metadata title)"
                        /usr/bin/playerctl -p "$i" play &
                        ;;
	       *) ;;
	    esac
        fi
done
