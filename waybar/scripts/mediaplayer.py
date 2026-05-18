#!/usr/bin/env python3
# waybar/scripts/mediaplayer.py
#
# outputs JSON for the custom/media waybar module
# shows currently playing track from any MPRIS-compatible player
# (spotify, firefox, vlc, mpv with mpris plugin, etc.)
#
# needs: playerctl (install: sudo pacman -S playerctl)
# usage: run this script — waybar calls it via "exec" in config.jsonc

import json
import subprocess
import sys


def get_playerctl(*args):
    """run a playerctl command and return stdout, or None on error"""
    try:
        result = subprocess.run(
            ["playerctl", *args],
            capture_output=True,
            text=True,
            timeout=3,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def main():
    player   = get_playerctl("--player=%any", "status")
    if not player or player.lower() not in ("playing", "paused"):
        sys.exit(0)

    status = player.lower()
    artist = get_playerctl("--player=%any", "metadata", "--format", "{{artist}}")
    title  = get_playerctl("--player=%any", "metadata", "--format", "{{title}}")
    player_name = get_playerctl("--player=%any", "metadata", "--format", "{{playerName}}")

    if not title:
        sys.exit(0)

    # build the display text
    if artist and artist != title:
        text = f"{artist} — {title}"
    else:
        text = title

    # truncate long strings
    max_len = 40
    if len(text) > max_len:
        text = text[: max_len - 1] + "…"

    # map player name to icon class (matches format-icons in config.jsonc)
    player_class = "default"
    if player_name:
        name_lower = player_name.lower()
        if "spotify" in name_lower:
            player_class = "spotify"
        elif "firefox" in name_lower or "chromium" in name_lower or "chrome" in name_lower:
            player_class = "firefox"

    # paused indicator
    if status == "paused":
        text = f"⏸ {text}"

    output = {
        "text":    text,
        "class":   f"custom-{player_class}",
        "alt":     player_class,
        "tooltip": f"{player_name or 'media'}: {text}",
    }

    print(json.dumps(output), flush=True)


if __name__ == "__main__":
    main()
