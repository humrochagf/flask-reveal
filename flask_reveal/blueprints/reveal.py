# -*- coding: utf-8 -*-
import glob

from flask import Blueprint, render_template, current_app


reveal_blueprint = Blueprint('reveal', __name__)


def load_slides():
    """
    Search the slide pages in the current directory, loading them in
    alphabetical order as a list of strings.

    The slide pages must be on markdown format having ".md" extension
    """

    slides = []

    for file in glob.glob('*.md'):
        with open(file, 'r') as sb:
            slides.append(sb.read())

    return slides


@reveal_blueprint.route("/")
def presentation():
    """
    View responsible to render the presentation

    TODO: Add style configuration
    """

    context = {
        'meta': current_app.config['META'],
        'slides': load_slides()
    }

    return render_template('presentation.html', **context)
