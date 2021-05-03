"""useful functions for the cli"""
from riordinato import Riordinato
from pathlib import Path
import typer
import json


def get_prefixes_file(ignore=False) -> Path:
    """Get the application configuration file"""
    app_dir = typer.get_app_dir('riordinato')
    config = Path(app_dir) / "config.json"

    if Path('prefixes.json').exists() and not ignore:
        file = 'prefixes.json'
        with open(file, 'r') as jfile:
            if not jfile.readlines():
                create_file(file)
    else:
        file = str(config)
        if not config.exists():
            config.touch()
        
        with open(file, 'r') as jfile:
            if not jfile.readlines():
                create_file(file)
    
    return file


def create_file(file):
    """Create the json file structure"""
    with open(file, 'w') as outfile:
        outfile.write(r"{}")


def get_data(file) -> dict:
    """Get the data from a json file"""
    with open(file, 'r') as jfile:
        data = json.load(jfile)

    return data


def show_common_files(source: Path, destination: Path):
    """check that there are no 2 files with the same name in two directories.

    Parameters
    ----------
    source: Path
        The directory where the repeated files are.
    destination: Path
        The second directory where it is to be compared with the first.
    """
    get_files = lambda path: [file.name for file in path.iterdir() if file.is_file()]
    files1 = get_files(source)
    files2 = get_files(destination)
    # Get the repeated files
    common_files = filter(lambda file: file in files2, files1)
    
    if common_files:
        dest_style = typer.style(f"{destination}", underline=True)
        typer.echo(f"These files already exists in the directory " + dest_style)
        for file in common_files:
            typer.secho(f"\t{file}", fg=typer.colors.RED)
        typer.echo("Consider renaming or removing it.")
   
