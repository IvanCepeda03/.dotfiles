
from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys

# Icons:
#   : nf-md-firefox
#   : nf-fa-code
#   : nf-cod-terminal
# 󰈙  : nf-md-file_document
# 󰕼  : nf-md-vlc
#   : nf-fa-discord
# 󰌨  : nf-md-layers

groups = [Group(i) for i in ["󰈹 ", " ", " ", "󰈙 ", "󰕼 ", " ", "󰌨 "]]

for i, group in enumerate(groups, 1):
    actual_key = str(i)
    keys.extend([
        Key(
            [mod],
            actual_key,
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        ),
        Key(
            [mod, "shift"],
            actual_key,
            lazy.window.togroup(group.name),
            desc="Move focused window to group {}".format(group.name)
        ),
        Key(
            [mod, "control"],
            actual_key,
            lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused windows to {}".format(group.name)
        )
    ]) 