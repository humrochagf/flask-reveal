# -*- coding: utf-8 -*-
from os import path

from flask import Flask

from .blueprints.reveal import reveal_blueprint


def create_app(presentation_path):
    """
    Create and configure the Flask app

    :param presentation_path: presentation directory
    :return: Flask app
    """

    current_dir = path.abspath(presentation_path)

    app = Flask('flask_reveal')

    # load default config
    app.config['CURRENT_DIR'] = current_dir
    app.config['MEDIA_ROOT'] = path.join(current_dir, 'img')

    app.config.from_object('flask_reveal.config')

    # load custom config
    try:
        app.config.from_pyfile(path.join(current_dir, 'config.py'))
    except FileNotFoundError:
        print('Configuration file "config.py" not found on current directory!')
        print('Loading slides without custom configurations...')

    app.register_blueprint(reveal_blueprint)

    return app
