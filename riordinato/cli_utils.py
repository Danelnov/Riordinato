"""useful functions for the cli"""
from riordinato import Riordinato
from pathlib import Path
import typer
import json


def get_config_file() -> Path:
    """Get the application configuration file"""
    app_dir = typer.get_app_dir('riordinato')
    config = Path(app_dir) / "config.json"
    if not config.exists():
        config.touch()
        create_file(str(config))

    return config

def create_file(file):
    """Create the json file structure"""
    with open(file, 'w') as outfile:
        json.dump({}, outfile, ensure_ascii=False, indent=4)


def get_data(file) -> dict:
    """Get the data from a json file"""
    with open(file, 'r') as jfile:
        data = json.load(jfile)

    return data
