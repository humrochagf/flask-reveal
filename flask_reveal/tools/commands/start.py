# -*- coding: utf-8 -*-
import os
import argparse

from flask_reveal.app import FlaskReveal


class Start(argparse.ArgumentParser):
    info = ({
        'prog': 'start',
        'description': 'starts a Flask Reveal presentation',
    })

    def __init__(self):
        super().__init__(**self.info)

        self.add_argument('path', nargs='?', default=os.getcwd())
        self.add_argument('-d', '--debug', action='store_true')

    def run(self, args=None):

        parse_result = self.parse_args(args)

        if os.path.isdir(parse_result.path):
            app = FlaskReveal('flask_reveal')

            app.start(os.path.abspath(parse_result.path), debug=parse_result.debug)
        else:
            raise NotADirectoryError('{0} is not a valid directory'.format(parse_result.path))

command = Start()
