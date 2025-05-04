from pathlib import Path

import click

from orm_maker.__version__ import __version__
from orm_maker.make_orm import make_orm_helper


@click.group()
def cli():
    pass


@cli.command()
def version():
    click.secho(f"ORM Maker v{__version__}")


@cli.command()
@click.argument("input", type=click.Path())
@click.argument("output", type=click.Path())
@click.option("--accept_changes", "-ac", is_flag=True, help="accept the proposed changes")
@click.option("--write_changes", "-wc", is_flag=True, help="overwrite the accepted changes onto the input path")
@click.option("--overwrite", "-o", is_flag=True, help="overwrite the output file")
@click.option(
    "--make_equals",
    "-me",
    is_flag=True,
    help="make the __eq__ function in the orm classes if 'id' is an attribute in the orm class or base class",
)
def make(
    input: Path,
    output: Path,
    accept_changes: bool = False,
    write_changes: bool = False,
    overwrite: bool = True,
    make_equals: bool = False,
) -> int:
    input = Path(input).resolve()
    output = Path(output).resolve()

    make_orm_helper(
        input=input,
        output=output,
        accept_changes=accept_changes,
        write_changes=write_changes,
        overwrite=overwrite,
        make_eq=make_equals,
    )

    return 0
