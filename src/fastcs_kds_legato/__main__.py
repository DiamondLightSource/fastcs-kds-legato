"""Interface for ``python -m fastcs_kds_legato``."""

from typing import Optional

import typer

from fastcs_kds_legato import __version__

__all__ = ["main"]

app = typer.Typer()


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


if __name__ == "__main__":
    app()
