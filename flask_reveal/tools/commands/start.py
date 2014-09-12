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

        self.path = os.getcwd()
        self.debug = False
        self.add_argument('path', nargs='?', default=self.path)
        self.add_argument('-d', '--debug', action='store_true')

    def parse_args(self, args=None, namespace=None):
        super().parse_args(args, self)

    def run(self, args=None):
        self.parse_args(args)

        if os.path.isdir(self.path):
            app = FlaskReveal('flask_reveal')

            app.start(os.path.abspath(self.path), debug=self.debug)
        else:
            raise NotADirectoryError('{0} is not a valid directory'.format(self.path))

command = Start()
