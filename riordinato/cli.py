"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
from .cli_utils import get_config_file, get_data, create_file

import json
import typer

from typing import List
from typing import Optional


app = typer.Typer()


@app.command()
def init():
    """
    Create prefixes.json file in current directory
    """
    file = Path.cwd() / "prefixes.json"
    if file.exists():
        typer.echo("The file already exists")
    else:
        create_file(str(file))
        typer.echo("The prefixes.json file was created")


@app.command()
def organize(
    ignore: bool = typer.Option(
        False, help="Ignore the prefixes.json file inside the directory", show_default=False),
    specific: Optional[List[str]] = typer.Option(
        None, help="Only move files containing these prefixes"),
    exclude: Optional[List[str]] = typer.Option(
        None, help="Ignore all files with these prefixes"),
):
    """
    Organize files that have prefixes
    """
    file = get_config_file(ignore)
    riordinato = Riordinato(Path.cwd())
    data = get_data(file)
    # Add prefixes to a Riordinato object
    for prefix, destination in data.items():
        riordinato.prefixes[prefix] = destination

    riordinato.movefiles(specific=specific, ignore=exclude)


@app.command(name='add')
def add_prefix(
    prefix: str = typer.Argument(
        ..., help="The prefix that the file names should have"),
    destination: Path = typer.Argument(
        ..., exists=True, help="The directory where the files with the prefix will be moved"),
    ignore: bool = typer.Option(
        False, help="Ignore the prefixes.json file inside the directory", show_default=False),
):
    """
    Add a new prefix to the json file
    """
    file = get_config_file(ignore)
    data = get_data(file)
    with open(file, 'w+') as jfile:
        # Add a prefix with an absolute path
        data[prefix] = str(destination.absolute())
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


@app.command(name='remove')
def remove_prefix(
    prefixes: List[str] = typer.Argument(
        ..., help="The prefixes to be removed from the database"),
    ignore: bool = typer.Option(
        False, help="Ignore the prefixes.json file inside the directory", show_default=False),
):
    """
    Remove prefixes
    """
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
