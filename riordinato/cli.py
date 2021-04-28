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


app = typer.Typer(help="Organize your files by prefixes.")


@app.command()
def init():
    """
    Create prefixes.json file in current directory.
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
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
    specific: Optional[List[str]] = typer.Option(
        None,
        help="Only move files containing these prefixes."
    ),
    exclude: Optional[List[str]] = typer.Option(
        None,
        help="Ignore all files with these prefixes."
    ),
):
    """
    Organize files that have prefixes.
    """
    try:
        file = get_prefixes_file(ignore)
        data = get_data(file)
        riordinato = Riordinato(Path.cwd())

        # get the amount of files in current directory
        # to later calculate the number of files that were organized
        def get_amount_files(): return len(
            [f for f in Path.cwd().iterdir() if f.is_file()])
        amount_files_before = get_amount_files()

        # Add prefixes to a Riordinato object
        for prefix, destination in data.items():
            riordinato.prefixes[prefix] = destination
        riordinato.movefiles(specific=specific, ignore=exclude)

        # calculate files that were organized
        amount_files_after = get_amount_files()
        amount_files = amount_files_before - amount_files_after
        typer.echo(f"{amount_files} files were organized")
    except FileNotFoundError:
        typer.echo(f"The directory '{destination}' does not exist.", err=True)
        typer.echo("If you want to delete it put the following command:")
        typer.secho(f"riordinato remove {prefix}", bold=True)


@app.command(name='add')
def add_prefix(
    prefix: str = typer.Argument(
        ...,
        help="The prefix that the file names should have."
    ),
    destination: Path = typer.Argument(
        ...,
        exists=True,
        help="The directory where the files with the prefix will be moved."
    ),
    ignore: bool = typer.Option(
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
):
    """
    Add a new prefix to the json file.
    """
    try:
        file = get_prefixes_file(ignore)
        data = get_data(file)

        with open(file, 'w+') as jfile:
            Prefix()[prefix] = destination  # check that the prefix is valid
            # Add a prefix with an absolute path
            data[prefix] = str(destination.absolute())
            # update the prefixes.json files
            jfile.write(json.dumps(data, ensure_ascii=False, indent=4))

        typer.echo(f"{prefix}:{destination} was added.")
    except InvalidPrefixError:
        typer.echo(f"{prefix} is an invalid prefix", err=True)


@app.command(name='remove')
def remove_prefix(
    prefixes: List[str] = typer.Argument(
        ...,
        help="The prefixes to be removed from the database."
    ),
    ignore: bool = typer.Option(
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
):
    """
    Remove prefixes.
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
