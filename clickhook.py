"""clickhook

Sketch for using click-based scripts with entry_points to create new commands
and to run hook functions in the main script
"""

import logging

from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins

logger = logging.getLogger(__name__)


@with_plugins(iter_entry_points('clickhook.new_commands'))
@click.group()
@click.pass_context
def main(ctx):
    """Main function"""
    logger.info('Starting clickhook')
    logger.info('invoked subcommand:', ctx.invoked_subcommand)


@main.command()
def run():
    """original command defined in script"""
    click.echo('running main command')
    for func in iter_entry_points('clickhook.run_commands'):
        func()
