"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
from .cli_utils import get_config_file, get_data
 
import json
import typer

from typing import List
from typing import Optional


app = typer.Typer()


@app.command()
def move(
    ignore: bool = False, 
    specific: Optional[List[str]] = None,
    exclude: Optional[List[str]] = None,
):
    """Command to move files containing some prefix"""
    file = get_config_file(ignore)
    riordinato = Riordinato(Path.cwd())
    data = get_data(file)
    # Add prefixes to a Riordinato object
    for prefix, destination in data.items():
        riordinato.prefixes[prefix] = destination

    riordinato.movefiles(specific=specific, ignore=exclude)


@app.command(name='add')
def add_prefix(
    prefix: str,
    destination: Path = typer.Argument(..., exists=True),
    ignore: bool = False,
):
    """Add a new prefix to the json file"""
    file = get_config_file(ignore)
    data = get_data(file)
    with open(file, 'w+') as jfile:
        # Add a prefix with an absolute path
        data[prefix] = str(destination.absolute())
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


@app.command(name='remove')
def remove_prefix(
    prefixes: List[str],
    ignore: bool = False,
):
    """Remove prefixes"""
    file = get_config_file(ignore)
    data = get_data(file)

    with open(file, 'w+') as jfile:
        # Remove the prefixes
        if prefixes[0] == '.':  # "." to remove all prefixes
            data = {}
        else:
            for prefix in prefixes:
                del data[prefix]
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
