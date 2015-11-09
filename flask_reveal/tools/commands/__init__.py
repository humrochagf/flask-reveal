# -*- coding: utf-8 -*-

import os
from importlib import import_module


def list_subcommands():
    try:
        return tuple([s[:-3] for s in os.listdir(os.path.dirname(__file__))
                      if not s.startswith('_') and s.endswith('.py')])
    except OSError:
        return tuple()


def load_subcomand(subcommand):
    module = 'flask_reveal.tools.commands.{0}'.format(subcommand)

    return import_module(module).command
