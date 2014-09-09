# -*- coding: utf-8 -*-
import os

from flask import Flask

from .blueprints.reveal import reveal_blueprint


class FlaskReveal(Flask):
    """
    Class that extends the Flask class loads the project specific configurations
    """

    def __init__(self, import_name, **kwargs):
        super(FlaskReveal, self).__init__(import_name, **kwargs)

        self.config.from_object('flask_reveal.config')
        self.register_blueprint(reveal_blueprint)

    def start(self, path, debug=False):
        """
        Starting method that handles configuration and starts the app

        :param path: path to presentation root
        :param debug: debug flag
        """
        self.config['PRESENTATION_ROOT'] = path
        self.config['MEDIA_ROOT'] = os.path.join(path, 'img')

        try:
            self.config.from_pyfile(os.path.join(path, 'config.py'))
        except FileNotFoundError:
            print('Configuration file "config.py" not found on current directory!')
            print('Loading slides without custom configurations...')

        self.run(debug=debug)
