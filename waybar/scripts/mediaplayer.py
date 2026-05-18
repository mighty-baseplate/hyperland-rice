#!/usr/bin/env python3
# outputs JSON for the waybar custom/media module
# needs: playerctl

import json
import subprocess
import sys


def playerctl(*args):
    try:
        r = subprocess.run(
            ["playerctl", *args],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            return r.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def main():
    status = playerctl("--player=%any", "status")
    if not status or status.lower() not in ("playing", "paused"):
        sys.exit(0)

    title       = playerctl("--player=%any", "metadata", "--format", "{{title}}")
    artist      = playerctl("--player=%any", "metadata", "--format", "{{artist}}")
    player_name = playerctl("--player=%any", "metadata", "--format", "{{playerName}}")

    if not title:
        sys.exit(0)

    text = f"{artist} — {title}" if artist and artist != title else title
    if len(text) > 40:
        text = text[:39] + "…"
    if status.lower() == "paused":
        text = f"⏸ {text}"

    cls = "default"
    if player_name:
        n = player_name.lower()
        if "spotify" in n:
            cls = "spotify"
        elif any(x in n for x in ("firefox", "chromium", "chrome")):
            cls = "firefox"

    print(json.dumps({
        "text":    text,
        "class":   f"custom-{cls}",
        "alt":     cls,
        "tooltip": f"{player_name or 'media'}: {text}",
    }), flush=True)


if __name__ == "__main__":
    main()
