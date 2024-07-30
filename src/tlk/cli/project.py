from pathlib import Path

from typer import Option, Typer
import copier
import typer

from tlk.constants import TEMPLATE_PATH


app = Typer(add_completion=False)   


@app.command()
def create(
    name: str = Option(..., "-n", "--name", help="Name of the python project / component."),
    python_version: str = Option(3.12, "-v", "--python-version", help="Python version."),
    poetry_version: str = Option(3.12, help="Poetry version."),
    destination: Path = Option(Path("."), help="Project / component root.")
) -> None:
    copier.run_copy(
        src_path=str(TEMPLATE_PATH / "project"),
        dst_path=str(destination),
        data={
            "name": name,
            "python_version": python_version,
            "poetry_version": poetry_version,
        },
        overwrite=False
    )
    typer.echo(f"Project '{name}' created successfully.")
