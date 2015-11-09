# -*- coding: utf-8 -*-

import argparse
import sys

import flask_reveal
from flask_reveal.tools.commands import list_subcommands, load_subcomand


class CLI(argparse.ArgumentParser):
    info = ({
        'prog': 'flaskreveal',
        'description': 'An easy way to make reveal.js presentations',
        'formatter_class': argparse.RawDescriptionHelpFormatter,
        'usage': '%(prog)s [-h|v] subcommand [options] [args]'
    })

    def __init__(self):
        super(CLI, self).__init__(**self.info)

        version = flask_reveal.__version__

        self.subcommand = None
        self.subcommands = list_subcommands()

        self.add_argument('subcommand')
        self.add_argument('-v', '--version',
                          action='version',
                          version='flask_reveal {0}'.format(version),
                          help='show the program version')

        self.epilog = '[subcommands]\n'

        for subcommand in self.subcommands:
            self.epilog += '    {0}\n'.format(subcommand)

    def parse_known_args(self, args=None, namespace=None):
        return super(CLI, self).parse_known_args(args, self)[1]

    def run(self, args=None):
        subcommand_args = self.parse_known_args(args)

        if self.subcommand in self.subcommands:
            command = load_subcomand(self.subcommand)

            command.run(subcommand_args)
        else:
            self.error('subcommand not found')


def cli_execute():
    cli = CLI()

    cli.run(sys.argv[1:])
