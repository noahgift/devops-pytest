import click

var=
@click.command()
@click.option('--name')
def marco(name):
    if name == "Marco":
        click.echo("Polo")
    else:
        click.echo("No Match")

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    marco()
