# -*- coding: utf-8 -*-
import sys
import argparse

from flask_reveal.tools.commands import list_subcommands, load_subcomand


class CLI(argparse.ArgumentParser):
    info = ({
        'prog': 'flaskreveal',
        'description': 'An easy way to make reveal.js presentations',
        'formatter_class': argparse.RawDescriptionHelpFormatter,
        'usage': '%(prog)s [-h] subcommand [options] [args]'
    })

    def __init__(self):
        super(CLI, self).__init__(**self.info)

        self.subcommand = None
        self.subcommand_list = list_subcommands()
        self.add_argument('subcommand')

        self.epilog = '[subcommands]\n'
        for subcommand in self.subcommand_list:
            self.epilog += '    {0}\n'.format(subcommand)

    def parse_known_args(self, args=None, namespace=None):
        return super(CLI, self).parse_known_args(args, self)[1]

    def run(self, args=None):
        subcommand_args = self.parse_known_args(args)

        if self.subcommand in self.subcommand_list:
            command = load_subcomand(self.subcommand)

            command.run(subcommand_args)
        else:
            self.error('subcommand not found')


def cli_execute():
    cli = CLI()

    cli.run(sys.argv[1:])
