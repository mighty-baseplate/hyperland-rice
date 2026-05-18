#!/bin/bash
# waybar/scripts/launch.sh — kill and restart waybar
# bound to SUPER+T in hyprland.conf (temporary — remove after setup)
# a cleaner way to toggle: SUPER+ALT+B sends SIGUSR1 to hide/show without restarting

killall -q waybar
sleep 0.2
waybar &
