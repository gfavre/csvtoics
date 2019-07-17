# -*- coding: utf-8 -*-

"""Console script for csvtoics."""
import sys
import click



@click.command()
@click.argument('filename')
def main(filename):
    from .csvtoics import export

    """Console script for csvtoics."""
    click.echo("Replace this message by putting your code into "
               "csvtoics.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    print(sys.argv)
    print(filename)
    destination = '/Users/grfavre/Desktop/exported.ics'
    export(filename, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
