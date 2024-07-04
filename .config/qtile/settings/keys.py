from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import qtile

from os import path

mod = "mod4"
terminal = "alacritty"
browser = "google-chrome-stable"

theme_selector_path = path.join(path.expanduser("~"), ".scripts", "theme-selector")
wallpaper_selector_path = path.join(path.expanduser("~"), ".scripts", "wallpaper-selector")

keys = [
    # WINDOWS
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # PROGRAMS
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Rofi Menu
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Opens a rofi menu for launching applications"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="Opens a rofi menu for selecting windows"),

    # Visuals Rofi-menus
    Key([mod, "shift"], "t", lazy.spawn(theme_selector_path), desc="Opens a rofi menu for selecting and changing the theme"),
    Key([mod, "shift"], "w", lazy.spawn(wallpaper_selector_path), desc="Opens a rofi menu for selecting and changing the wallpaper"),

    # Browser
    Key([mod], "b", lazy.spawn(browser), desc="Opens a browser"),

    # File Explorer
    Key([mod], "e", lazy.spawn("thunar"), desc="Opens a browser"),

    # UTILITIES
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"), desc="Raise the system volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5"), desc="Lower the system volume"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Toggle mute"),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Raise the brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Lower the brightness")

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )