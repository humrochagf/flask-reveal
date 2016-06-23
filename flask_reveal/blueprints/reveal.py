# -*- coding: utf-8 -*-

import glob
import os

from flask import (Blueprint, current_app, render_template,
                   send_from_directory, url_for)

REVEAL_CONFIG = current_app.config.get('REVEAL_CONFIG')


reveal_blueprint = Blueprint('reveal', __name__)


def load_markdown_slide(path):
    """
    Get slides file in the current directory, load it and split 
    it into list of slides.

    The slide page must be on markdown format having ".md" extension.
    Slide separator must be defined into `config.py`

    :return: a list of strings with the slides content
    """

    with open(os.path.join(path, 'slides.md'), 'r') as sb:
        slides = sb.read()

    return slides.split(REVEAL_CONFIG.get('slideSep', '---'))


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
    slides = load_markdown_slide(current_app.config.get('PRESENTATION_ROOT'))
    config = current_app.config.get('REVEAL_CONFIG')
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
