# -*- coding: utf-8 -*-
from _pickle import load
from flask import Blueprint, render_template, current_app

from .utils import load_markdown_slides


reveal_blueprint = Blueprint('reveal', __name__)


@reveal_blueprint.route("/")
def presentation():
    """
    View responsible to render the presentation

    TODO: Add style configuration
    """

    context = {
        'meta': current_app.config['META'],
        'slides': load_markdown_slides()
    }

    return render_template('presentation.html', **context)
