"""Cli app for riordinato"""
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

def main():
    app()
