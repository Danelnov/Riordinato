"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
from typing import Optional
import json
import typer


def get_config_file():
    app_dir = typer.get_app_dir('riordinato')
    config = Path(app_dir) / "config.json"
    if not config.exists():
        config.touch()
        


app = typer.Typer()


@app.command()
def move(prefix: str, destination: Path):
    try:
        instance = Riordinato(Path.cwd())
        instance.prefixes[prefix] = destination
        instance.movefiles(specific=prefix)
        typer.secho(f"Done!", fg=typer.colors.GREEN, bold=True)
    except:
        typer.secho("Error", fg=typer.colors.RED, bold=True)


@app.command(name='add')
def add_prefix(
    prefix: str,
    destination: str,
    file: str = typer.Option('prefixes.json', '--file', '-f')
):
    with open(file, 'r') as jfile:
        data = json.load(jfile)
    with open(file, 'w+') as jfile:
        data[prefix] = destination
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
