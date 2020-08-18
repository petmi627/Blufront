#!/bin/bash

for i in $(playerctl -l);
do
	player_status=$(/usr/bin/playerctl -p "$i" status 2> /dev/null)
	if [[ $? -eq 0 ]]; then
	    case $player_status in
                Playing|Paused)
        	        artist="$(/usr/bin/playerctl -p $i metadata artist)"
         	        if [[ artist -eq "" ]]; then
         		    metadata="$(/usr/bin/playerctl -p $i metadata title)"
    	                else
	                    metadata="$artist - $(/usr/bin/playerctl -p $i metadata title)"
                        fi
                	;;
	       *) ;;
	    esac
        fi
done

if [[ $(echo $metadata | wc -c) -gt 35 ]]; then
    output=$(echo $metadata | cut -c 1-35)"..."
else
    output=$metadata
fi

# Foreground color formatting tags are optional
if [[ $player_status = "Playing" ]]; then
    echo "%{F#FFFFFF}▶ $output%{F-}"
elif [[ $player_status = "Paused" ]]; then
    echo "%{F#999}$output%{F-}"
else
    echo ""
fi
