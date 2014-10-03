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
        self.media = None
        self.debug = False
        self.add_argument('path', nargs='?', default=self.path)
        self.add_argument('-m', '--media',  default=self.media)
        self.add_argument('-d', '--debug', action='store_true')

    def parse_args(self, args=None, namespace=None):
        super().parse_args(args, self)

    def run(self, args=None):
        self.parse_args(args)

        if os.path.isdir(self.path):
            self.path = os.path.abspath(self.path)

            if not self.media:
                self.media = os.path.join(self.path, 'img')

            if os.path.isdir(self.media):
                app = FlaskReveal('flask_reveal')

                app.start(self.path, media_root=self.media, debug=self.debug)
            else:
                raise NotADirectoryError('your media path {0} is not a valid directory'.format(self.media))
        else:
            raise NotADirectoryError('your presentation path {0} is not a valid directory'.format(self.path))

command = Start()
