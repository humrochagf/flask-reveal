# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, current_app, send_from_directory

from .utils import load_markdown_slides


reveal_blueprint = Blueprint('reveal', __name__)


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

    TODO: Add style configuration
    """

    context = {
        'meta': current_app.config.get('REVEAL_META'),
        'slides': load_markdown_slides(),
        'config': current_app.config.get('REVEAL_CONFIG'),
        'theme': current_app.config.get('REVEAL_THEME'),
    }
    
    return render_template('presentation.html', **context)
