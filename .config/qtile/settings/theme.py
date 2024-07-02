import json

from .path import qtile_path

from os import path

def load_theme():
    default_theme = "dark-grey"
    default_theme_data = {
        "theme": "dark-grey"
    }

    config = path.join(path.expanduser("~"), ".config", ".theme", "config.json")

    if path.isfile(config):
        with open(config) as f:
            theme = json.load(f)["theme"]
    else:
        with open(config, "w") as f:
            json.dump(default_theme_data, f, indent=4)

    theme_file = path.join(qtile_path, "themes", theme + ".json")
    if not path.isfile(theme_file):
        raise Exception(f'{theme_file} does not exist')
    
    with open(theme_file, "r") as f:
        return json.load(f)

if __name__ == "settings.theme":
    colors = load_theme()
