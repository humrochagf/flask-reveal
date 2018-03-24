# -*- coding: utf-8 -*-

import argparse
import os
import shutil

import flask_reveal.config as config


class MkPresentation(argparse.ArgumentParser):
    info = ({
        'prog': 'mkpresentation',
        'description': 'create the presentation directory structure',
    })

    def __init__(self):
        super(MkPresentation, self).__init__(**self.info)

        self.path = 'my_presentation'
        self.add_argument('path', nargs='?', default=self.path)

    def parse_args(self, args=None, namespace=None):
        super(MkPresentation, self).parse_args(args, self)

    def run(self, args=None):
        self.parse_args(args)

        config_file = os.path.join(os.path.dirname(config.__file__),
                                   'config.py')

        if not os.path.exists(self.path):
            presentation_name = os.path.basename(self.path)

            os.mkdir(self.path)  # Presentation dir
            os.mkdir(os.path.join(self.path, 'img'))  # Images dir
            shutil.copy(config_file, self.path)  # Config file
            # First slide file
            with open(os.path.join(self.path, 'slides.md'), 'w') as f:
                f.write('# {0}\n\nStart from here!'.format(
                    presentation_name.replace('_', ' ').title()))
        else:
            self.error('{0} folder already exists'.format(self.path))


command = MkPresentation()
