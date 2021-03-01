"""Cli app for riordinato"""
from pathlib import Path
from riordinato import Riordinato
import typer

app = typer.Typer()

@app.command()
def move(prefix: str, destination: Path):
    instance = Riordinato(Path.cwd())
    instance.prefixes[prefix] = destination
    instance.movefiles(specific=prefix)
    typer.echo(f"files with prefix {prefix} were moved to destination {destination}")

@app.command()
def current_dir():
    typer.echo(Path.cwd())

def main():
    app()
