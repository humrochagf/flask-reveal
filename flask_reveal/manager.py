# -*- coding: utf-8 -*-
"""flask-reveal

Usage:
    flaskreveal start [-d | --debug]
    flaskreveal start [-d | --debug] PATH
    flaskreveal mkpresentation
    flaskreveal mkpresentation NAME
    flaskreveal installreveal
    flaskreveal installreveal -f FILE
    flaskreveal installreveal -u URL
    flaskreveal -h | --help

Options:
    -d --debug              Start flask with debug mode on.
    -f FILE --file=FILE     Reveal.js .tar.gz or .zip release file.
    -u URL --url=URL        Url of reveal.js .tar.gz or .zip release file.
    -h --help               Show this help.

"""
import sys
from docopt import docopt

from flask_reveal.tools.commands.start import Start
from flask_reveal.tools.commands.mkpresentation import MkPresentation
from flask_reveal.tools.commands.installreveal import InstallReveal


def cli_execute():
    arguments = docopt(__doc__)

    if arguments['start']:
        command = Start()

        command.run(sys.argv[2:])

    elif arguments['mkpresentation']:
        command = MkPresentation()

        command.run(sys.argv[2:])

    elif arguments['installreveal']:
        command = InstallReveal()

        command.run(sys.argv[2:])
