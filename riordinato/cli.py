"""Cli app for riordinato"""

from riordinato.exceptions import InvalidPrefixError
from .cli_utils import get_prefixes_file, get_data, create_file
from riordinato import Riordinato
from riordinato import Prefix

import json
import typer

from pathlib import Path
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
        typer.secho("The prefixes.json file was created.",
                    fg=typer.colors.GREEN)


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
    file = get_prefixes_file(ignore)
    data = get_data(file)
    riordinato = Riordinato(Path.cwd())

    # get the amount of files in current directory
    # to later calculate the number of files that were organized
    get_amount_files = lambda: len([f for f in Path.cwd().iterdir() if f.is_file()])
    amount_files_before = get_amount_files()
    
    # Add prefixes to a Riordinato object
    for prefix, destination in data.items():
        riordinato.prefixes[prefix] = destination
    riordinato.movefiles(specific=specific, ignore=exclude)

    # calculate files that were organized
    amount_files_after = get_amount_files()
    amount_files = amount_files_before - amount_files_after
    typer.secho(f"{amount_files} files were organized", fg=typer.colors.GREEN)


@app.command(name='add')
def add_prefix(
    prefix: str = typer.Argument(
        ..., help="The prefix that the file names should have"),
    destination: Path = typer.Argument(
        ..., help="The directory where the files with the prefix will be moved", exists=True),
    ignore: bool = typer.Option(
        False, help="Ignore the prefixes.json file inside the directory", show_default=False),
):
    """
    Add a new prefix to the json file
    """
    try:
        file = get_prefixes_file(ignore)
        data = get_data(file)

        with open(file, 'w+') as jfile:
            Prefix()[prefix] = destination # check that the prefix is valid
            data[prefix] = str(destination.absolute()) # Add a prefix with an absolute path
            # update the prefixes.json files
            jfile.write(json.dumps(data, ensure_ascii=False, indent=4))

        typer.secho(f"{prefix}:{destination} was added.", fg=typer.colors.GREEN)
    except InvalidPrefixError:
        typer.echo(f"{prefix} is an invalid prefix", err=True)


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
    file = get_prefixes_file(ignore)
    data = get_data(file)

    with open(file, 'w+') as jfile:
        # Remove the prefixes
        if prefixes[0] == '.':  # "." to remove all prefixes
            data = {}
        else:
            for prefix in prefixes:
                del data[prefix]
        # update the prefixes.json files
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
