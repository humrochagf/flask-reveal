# -*- coding: utf-8 -*-

import glob
import os

from flask import Blueprint, current_app, render_template, send_from_directory


reveal_blueprint = Blueprint('reveal', __name__)


def load_markdown_slides(path):
    """
    Search the slide pages in the current directory, loading them in
    alphabetical order as a list of strings.

    The slide pages must be on markdown format having ".md" extension

    :return: a list of strings with the slides content
    """

    slides = []

    for slide in sorted(glob.glob(os.path.join(path, '*.md'))):
        with open(slide, 'r') as sb:
            slides.append(sb.read())

    return slides


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
    slides = load_markdown_slides(current_app.config.get('PRESENTATION_ROOT'))
    config = current_app.config.get('REVEAL_CONFIG')

    context = {
        'meta': meta,
        'slides': slides,
        'config': config,
    }

    return render_template('presentation.html', **context)
