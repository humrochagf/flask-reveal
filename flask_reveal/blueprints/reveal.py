# -*- coding: utf-8 -*-
import os
import glob

from flask import Blueprint, render_template, current_app, send_from_directory


reveal_blueprint = Blueprint('reveal', __name__)


def load_markdown_slides(path):
    """
    Search the slide pages in the current directory, loading them in
    alphabetical order as a list of strings.

    The slide pages must be on markdown format having ".md" extension

    :return: a list of strings with the slides content
    """

    slides = []

    for file in sorted(glob.glob(os.path.join(path, '*.md'))):
        with open(file, 'r') as sb:
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

    context = {
        'meta': current_app.config.get('REVEAL_META'),
        'slides': load_markdown_slides(current_app.config.get('PRESENTATION_ROOT')),
        'config': current_app.config.get('REVEAL_CONFIG'),
    }
    
    return render_template('presentation.html', **context)
