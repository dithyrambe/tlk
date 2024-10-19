from rich.console import Console
from typer import Typer
import typer

from tlk.constants import PACKAGE_NAME
from tlk.cli.project import app as project_app


app = Typer(add_completion=False)
app.add_typer(project_app, name="project")


def show_version(flag: bool):
    if flag:
        from importlib.metadata import version

        console = Console()
        console.print(f"release [bold]{version(PACKAGE_NAME)}[bold]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None, "--version", callback=show_version, help="Show version."
    ),
):
    """Make release"""
