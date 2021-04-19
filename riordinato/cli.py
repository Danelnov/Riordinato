"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
import json
import typer

import riordinato


app = typer.Typer()


@app.command()
def move(file: str = typer.Option('prefixes.json', '--file', '-f')):
    riordinato = Riordinato(Path.cwd())
    with open(file, 'r') as jfile:
        data = json.load(jfile)
        for prefix, destination in data.items():
            riordinato.prefixes[prefix] = destination
    
    riordinato.movefiles()


@app.command(name='add')
def add_prefix(
    prefix: str,
    destination: Path = typer.Argument(..., exists=True),
    file: str = typer.Option('prefixes.json', '--file', '-f')
):
    with open(file, 'r') as jfile:
        data = json.load(jfile)
    with open(file, 'w+') as jfile:
        data[prefix] = str(destination.absolute())
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


@app.command(name='remove')
def remove_prefix(
    prefix: str,
    file: str = typer.Option('prefixes.json', '--file', '-f')
):
    with open(file, 'r') as jfile:
        data = json.load(jfile)
    with open(file, 'w+') as jfile:
        del data[prefix]
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
