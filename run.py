# -*- coding: utf-8 -*-
'''flask-reveal

Usage:
    run.py start [-d | --debug] [-p | --path PATH]
    run.py (-h | --help)

Options:
    -d --debug          Start flask with debug mode on.
    -p --path PATH      Presentation directory [default: ./].
    -h --help           Show this help.

'''

import os

from docopt import docopt

from flask_reveal.app import create_app


def start(path, debug):
    if os.path.isdir(path):
        app = create_app(path)

        app.run(debug=debug)
    else:
        print('This is not a valid directory')


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['start']:
        start(arguments['--path'][0], arguments['--debug'])
