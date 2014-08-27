# -*- coding: utf-8 -*-
from os import path

from flask import Flask

from .blueprints.reveal import reveal_blueprint


def create_app(config_filename=None):
    instance_path = path.abspath(path.curdir)
    app = Flask('flask_reveal',
                instance_path=instance_path,
                instance_relative_config=True)

    # load default config
    app.config.from_object('flask_reveal.settings')
    app.config['MEDIA_ROOT'] = path.join(instance_path, 'img')

    # load custom config
    try:
        app.config.from_pyfile('config.cfg')
    except FileNotFoundError:
        print('Configuration file "config.cfg" not found on current directory!')
        print('Loading slides without custom configurations...')

    app.register_blueprint(reveal_blueprint)

    return app
