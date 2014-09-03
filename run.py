# -*- coding: utf-8 -*-
"""flask-reveal

Usage:
    run.py start [-d | --debug] [-p | --path PATH]
    run.py installreveal (-f | --file FILE)
    run.py (-h | --help)

Options:
    -d --debug          Start flask with debug mode on.
    -p --path PATH      Presentation directory [default: ./].
    -f --file FILE      Reveal.js .tar.gz or .zip release file.
    -h --help           Show this help.

"""

import os
import shutil
import tarfile
import zipfile

from docopt import docopt

from flask_reveal.app import create_app


def start(path, debug):
    """
    Starting flask app function

    :param path: path to the presentation folder
    :param debug: debug flag
    """

    if os.path.isdir(path):
        app = create_app(path)

        app.run(debug=debug)
    else:
        print('This is not a valid directory')


def move_and_replace(src, dst):
    """
    Helper function used to move files from one place to another, creating os replacing them if needed

    :param src: source directory
    :param dst: destination directory
    """

    src = os.path.abspath(src)
    dst = os.path.abspath(dst)

    for src_dir, dirs, files in os.walk(src):  # using os walk to navigate through the directory tree
        # keep te dir structure by replacing the source root to the destination on walked path
        dst_dir = src_dir.replace(src, dst)

        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)  # to copy not fail, create the not existing dirs

        for file in files:
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_dir, file)

            if os.path.exists(dst_file):
                os.remove(dst_file)  # to copy not fail, create existing files

            shutil.move(src_file, dst_dir)  # move the files

    shutil.rmtree(src)  # remove the dir structure from the source


def install_reveal_from_file(file):
    """
    Install reveal from a given .tar.gz or .zip file

    :param file: reveal.js distribution file
    """

    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'flask_reveal/static/'))

    if os.path.isfile(file):
        if tarfile.is_tarfile(file):
            with tarfile.open(file, 'r:gz') as tfile:
                basename = tfile.members[0].name
                tfile.extractall()

            move_and_replace(basename, static_folder)
        elif zipfile.is_zipfile(file):
            with zipfile.ZipFile(file, 'r') as zfile:
                basename = zfile.namelist()[0]
                zfile.extractall()

            move_and_replace(basename, static_folder)
        else:
            print('File type not supported')
    else:
        print('This is not a valid file')

if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['start']:
        start(arguments['--path'][0], arguments['--debug'])
    elif arguments['installreveal']:
        install_reveal_from_file(arguments['--file'][0])