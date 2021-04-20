"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
from .cli_utils import get_config_file, get_data
from typing import List
import json
import typer


app = typer.Typer()


@app.command()
def move(
    ignore: bool = False,
):
    file = get_config_file(ignore)
    riordinato = Riordinato(Path.cwd())
    data = get_data(file)
    for prefix, destination in data.items():
        riordinato.prefixes[prefix] = destination

    riordinato.movefiles()


@app.command(name='add')
def add_prefix(
    prefix: str,
    destination: Path = typer.Argument(..., exists=True),
    ignore: bool = False,
):
    file = get_config_file(ignore)
    data = get_data(file)
    with open(file, 'w+') as jfile:
        data[prefix] = str(destination.absolute())
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


@app.command(name='remove')
def remove_prefix(
    prefixes: List[str],
    ignore: bool = False,
):
    file = get_config_file(ignore)
    data = get_data(file)
    with open(file, 'w+') as jfile:
        if prefixes[0] == '.':
            data = {}
        else:
            for prefix in prefixes:
                del data[prefix]
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
