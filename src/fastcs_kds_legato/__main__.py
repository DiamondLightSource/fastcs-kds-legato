"""Interface for ``python -m fastcs_kds_legato``."""

from pathlib import Path
from typing import Optional

import typer
from fastcs.connections import SerialConnectionSettings
from fastcs.launch import FastCS
from fastcs.transport.epics.ca.options import EpicsCAOptions
from fastcs.transport.epics.options import EpicsGUIOptions, EpicsIOCOptions

from fastcs_kds_legato import __version__
from fastcs_kds_legato.kds_legato_controller import KdsLegatoController

__all__ = ["main"]

app = typer.Typer()

OPI_PATH = Path("/epics/opi")


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    # TODO: typer does not support `bool | None` yet
    # https://github.com/tiangolo/typer/issues/533
    version: Optional[bool] = typer.Option(  # noqa
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Print the version and exit",
    ),
):
    pass


@app.command()
def ioc(pv_prefix: str = typer.Argument()):
    ui_path = OPI_PATH if OPI_PATH.is_dir() else Path.cwd()

    connection_settings = SerialConnectionSettings("192.168.1.6:7004", 460800)
    # Create a controller instance
    controller = KdsLegatoController(connection_settings)

    # IOC options
    options = EpicsCAOptions(
        ca_ioc=EpicsIOCOptions(pv_prefix=pv_prefix),
        gui=EpicsGUIOptions(
            output_path=ui_path / "kds_legato.bob", title=f"KDS_LEGATO - {pv_prefix}"
        ),
    )

    # ...and pass them both to FastCS
    launcher = FastCS(controller, [options])
    launcher.create_docs()
    launcher.create_gui()
    launcher.run()


if __name__ == "__main__":
    app()
