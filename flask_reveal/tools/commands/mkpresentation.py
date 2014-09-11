# -*- coding: utf-8 -*-
import os
import shutil
import argparse

import flask_reveal.config as config


class MkPresentation(argparse.ArgumentParser):
    info = ({
        'prog': 'mkpresentation',
        'description': 'create the presentation directory structure',
    })

    def __init__(self):
        super().__init__(**self.info)

        self.add_argument('name', nargs='?', default='my_presentation')

    def run(self, args=None):

        parse_result = self.parse_args(args)

        presentation_path = parse_result.name
        config_file = os.path.join(os.path.dirname(config.__file__), 'config.py')

        if not os.path.exists(presentation_path):
            presentation_name = os.path.basename(presentation_path)

            os.mkdir(presentation_path)  # Presentation dir
            os.mkdir(os.path.join(presentation_path, 'img'))  # Images dir
            shutil.copy(config_file, presentation_path)  # Config file
            # First slide file
            with open(os.path.join(presentation_path, 'slide000.md'), 'w') as f:
                f.write('# {0}\n\nStart from here!'.format(presentation_name.replace('_', ' ').title()))
        else:
            raise FileExistsError('{0} folder already exists'.format(presentation_path))

command = MkPresentation()
