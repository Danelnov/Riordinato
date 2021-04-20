"""useful functions for the cli"""
from riordinato import Riordinato
from pathlib import Path
import typer
import json


def get_config_file(ignore=False) -> Path:
    """Get the application configuration file"""
    app_dir = typer.get_app_dir('riordinato')
    config = Path(app_dir) / "config.json"

    if Path('prefixes.json').exists() and not ignore:
        file = 'prefixes.json'
        with open(file, 'r') as jfile:
            if not jfile.readlines():
                create_file(file)
    else:
        file = str(config)
        if not config.exists():
            config.touch()
        
        with open(file, 'r') as jfile:
            if not jfile.readlines():
                create_file(file)
    
    return file


def create_file(file):
    """Create the json file structure"""
    with open(file, 'w') as outfile:
        outfile.write(r"{}")


def get_data(file) -> dict:
    """Get the data from a json file"""
    with open(file, 'r') as jfile:
        data = json.load(jfile)

    return data
