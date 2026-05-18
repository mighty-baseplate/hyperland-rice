# hyprland rice

my hyprland setup on arch. catppuccin mocha theme.

![bar sits at the bottom of the screen, floating pill style]

## what's included

```
hypr/
  hyprland.conf         main config

waybar/
  config.jsonc          module layout
  style.css             catppuccin mocha theme
  scripts/
    mediaplayer.py      MPRIS wrapper for the media module
    launch.sh           kill and restart waybar
```

## dependencies

| tool | what it does |
|------|-------------|
| hyprland | compositor |
| waybar | status bar |
| kitty | terminal |
| swww | wallpaper daemon |
| wofi | app launcher |
| playerctl | media controls |
| grimblast | screenshots |
| hyprlock | lock screen |
| safeeyes | break reminders |
| brightnessctl | brightness keys |

install on arch:
```sh
sudo pacman -S hyprland waybar kitty swww wofi playerctl brightnessctl
yay -S grimblast-git hyprlock safeeyes
```

## setup

```sh
git clone https://github.com/mighty-baseplate/hyperland-rice
cd hyperland-rice

cp -r hypr ~/.config/
cp -r waybar ~/.config/
cp .zshrc ~/
```

then log into a hyprland session.

## keybinds

| bind | action |
|------|--------|
| `SUPER + Return` | terminal |
| `SUPER + R` | launcher |
| `SUPER + C` | close window |
| `SUPER + V` | toggle float |
| `SUPER + F` | fullscreen |
| `SUPER + L` | lock screen |
| `SUPER + S` | scratchpad |
| `SUPER + [1-0]` | switch workspace |
| `SUPER + SHIFT + [1-0]` | move window to workspace |
| `SUPER + ALT + R` | resize mode (use arrows, ESC to exit) |
| `SUPER + ALT + B` | toggle waybar |
| `Print` | screenshot area |
| `SHIFT + Print` | screenshot full screen |

## known issues / todo

- [ ] hyprlock config not included — lock screen won't work until you add one
- [ ] notifications need dunst or mako set up separately
- [ ] clipboard history (cliphist) uncomment in autostart + keybind to enable
- [ ] wallpaper doesn't auto-set — run `swww img <path>` after login
