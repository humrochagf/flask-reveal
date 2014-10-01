# -*- coding: utf-8 -*-
import glob
import os


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