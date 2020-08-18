#!/bin/bash
i3-msg "workspace 1; append_layout ~/.config/i3/layout_terminal.json"

i3-msg kill

(gnome-terminal &)
(gnome-terminal --title "Htop" -- htop &)
(gnome-terminal --title "Cmatrix" -- cmatrix &)
(gnome-terminal --title "Vis" -- vis &)

