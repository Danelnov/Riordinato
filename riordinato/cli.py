"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
import typer

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


@app.command()
def current_dir():
    typer.echo(Path.cwd())


def main():
    app()
