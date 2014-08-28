# -*- coding: utf-8 -*-
from os import path

from flask import Flask

from .blueprints.reveal import reveal_blueprint


def create_app():
    current_dir = path.abspath(path.curdir)

    app = Flask('flask_reveal')

    # load default config
    app.config['CURRENT_DIR'] = current_dir
    app.config['MEDIA_ROOT'] = path.join(current_dir, 'img')

    app.config.from_object('flask_reveal.settings')

    # load custom config
    try:
        app.config.from_pyfile(path.join(current_dir, 'config.cfg'))
    except FileNotFoundError:
        print('Configuration file "config.cfg" not found on current directory!')
        print('Loading slides without custom configurations...')

    app.register_blueprint(reveal_blueprint)

    return app
