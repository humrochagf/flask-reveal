# -*- coding: utf-8 -*-

import glob

from flask import Flask, render_template


server = Flask(__name__)


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


def load_meta():
    """
    Load the meta content

    TODO: Make them read from a external config file
    """

    meta = {
        'title': 'The title',
        'author': 'Some Author',
        'description': 'Some description'
    }

    return meta


@server.route("/")
def presentation():
    """
    View responsible to render the presentation

    TODO: Add style configuration
    """

    context = {
        'meta': load_meta(),
        'slides': load_slides()
    }

    return render_template('presentation.html', **context)
