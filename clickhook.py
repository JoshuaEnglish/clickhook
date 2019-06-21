"""clickhook

Sketch for using click-based scripts with entry_points to create new commands
and to run hook functions in the main script
"""

import logging

from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

logging.root.setLevel(logging.NOTSET)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter('%(name)s:%(levelname)s:%(message)s'))
console.setLevel(logging.DEBUG)
logging.root.addHandler(console)


class Library:
    pass


global_lib = Library()


@with_plugins(iter_entry_points('clickhook.new_commands'))
@click.group()
@click.pass_context
def main(ctx):
    """Main function"""
    logging.info('Starting clickhook')
    logging.info(f'invoked subcommand: {ctx.invoked_subcommand}')
    logging.info(f'ctx object is {ctx}')
    ctx.obj = {'lib': global_lib}
    logging.info(f"main library in context: {ctx.obj['lib']}")


@main.command()
@click.pass_context
def run(ctx):
    """original command defined in script"""
    logging.info('running main command')
    click.echo('running main command')
    for entry_point in iter_entry_points('clickhook.run_commands'):
        func = entry_point.load()
        func(ctx)
