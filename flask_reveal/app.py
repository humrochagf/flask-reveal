# -*- coding: utf-8 -*-
from os import path

from flask import Flask

from .blueprints.reveal import reveal_blueprint


class FlaskReveal(Flask):
    """
    Class that extends the Flask class loads the project specific configurations
    """

    def __init__(self, presentation_path, import_name, **kwargs):
        super(FlaskReveal, self).__init__(import_name, **kwargs)

        self.config['PRESENTATION_ROOT'] = presentation_path
        self.config['MEDIA_ROOT'] = path.join(presentation_path, 'img')

        self.config.from_object('flask_reveal.config')

        try:
            self.config.from_pyfile(path.join(presentation_path, 'config.py'))
        except FileNotFoundError:
            print('Configuration file "config.py" not found on current directory!')
            print('Loading slides without custom configurations...')

        self.register_blueprint(reveal_blueprint)
