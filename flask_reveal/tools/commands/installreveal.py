# -*- coding: utf-8 -*-

import argparse
import os

try:
    # python 3
    from urllib.request import urlretrieve
except ImportError:
    # python 2
    from urllib import urlretrieve

import flask_reveal
from flask_reveal.tools.helpers import extract_file, move_and_replace


class InstallReveal(argparse.ArgumentParser):
    info = ({
        'prog': 'installreveal',
        'description': 'installs Reveal.js',
    })

    def __init__(self):
        super(InstallReveal, self).__init__(**self.info)

        self.url = None
        self.path = None
        self.add_argument('-u', '--url', action='store')
        self.add_argument('-p', '--path', action='store')

    def parse_args(self, args=None, namespace=None):
        super(InstallReveal, self).parse_args(args, self)

        if not self.url and not self.path:
            self.url = ('https://github.com/hakimel/reveal.js/' +
                        'archive/3.6.0.tar.gz')

    def run(self, args=None):
        self.parse_args(args)

        print('Downloading reveal.js...')

        if self.url:
            try:
                response = urlretrieve(self.url)
                self.path = response[0]
            except Exception:
                raise

        print('Installing reveal.js...')

        move_and_replace(
            extract_file(self.path),
            os.path.join(os.path.dirname(flask_reveal.__file__), 'static/')
        )

        print('Installation complete!')


command = InstallReveal()
