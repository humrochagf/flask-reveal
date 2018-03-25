# -*- coding: utf-8 -*-

import re

from flask import (Blueprint, current_app, render_template,
                   send_from_directory, url_for)

reveal_blueprint = Blueprint('reveal', __name__)


def load_markdown_slide(path, separator):
    """
    Get slides file from the given path, loads it and split into list
    of slides.

    The slide page must be on markdown format having ".md" extension.
    Slide separator must be defined into `config.py`

    :return: a list of strings with the slides content
    """

    with open(path, 'r') as slides_file:
        slides = slides_file.read()

    return re.split('^{}$'.format(separator), slides, flags=re.MULTILINE)


@reveal_blueprint.route('/img/<path:filename>')
def get_img(filename):
    """
    View to render the image file on the slide

    :param filename: the image filename from the request
    :return: the image resource
    """

    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)


@reveal_blueprint.route('/')
def presentation():
    """
    View responsible to render the presentation
    """

    meta = current_app.config.get('REVEAL_META')
    config = current_app.config.get('REVEAL_CONFIG')
    slides = load_markdown_slide(current_app.config.get('PRESENTATION_FILE'),
                                 config.get('slideSep', '---'))
    theme = (url_for('static', filename='css/theme/') +
             current_app.config.get('REVEAL_THEME') +
             '.css')

    context = {
        'meta': meta,
        'slides': slides,
        'config': config,
        'theme': theme,
    }

    return render_template('presentation.html', **context)
