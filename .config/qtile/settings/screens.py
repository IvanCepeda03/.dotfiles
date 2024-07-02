from libqtile.config import Screen
from libqtile import bar

from os import path

from settings.widgets import primary_widgets
from settings.widgets import secondary_widgets

def status_bar(widgets):
    return bar.Bar(widgets, 26, opacity=0.95)

# TODO Add multi-monitor automatic support

screens = [
    # Primary Screen
    Screen(top=status_bar(primary_widgets)),
    # Second Screen
    Screen(top=status_bar(secondary_widgets))
]