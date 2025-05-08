import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
def hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    cli()
