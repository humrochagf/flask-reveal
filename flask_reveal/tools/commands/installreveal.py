# -*- coding: utf-8 -*-
import os
import argparse
from urllib import request

import flask_reveal
from flask_reveal.tools.helpers import move_and_replace, extract_file


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

    def run(self, args=None):
        self.parse_args(args)

        if not self.url and not self.path:
            self.url = 'https://github.com/hakimel/reveal.js/' + \
                       'archive/2.6.2.tar.gz'

        if self.url:
            try:
                response = request.urlretrieve(self.url)
                self.path = response[0]
            except Exception:
                raise

        move_and_replace(
            extract_file(self.path),
            os.path.join(os.path.dirname(flask_reveal.__file__), 'static/')
        )

command = InstallReveal()
