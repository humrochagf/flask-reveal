# -*- coding: utf-8 -*-
'''flask-reveal

Usage:
    run.py start [-d | --debug] [-p | --path PATH]
    run.py installreveal [-f | --file FILE]
    run.py (-h | --help)

Options:
    -d --debug          Start flask with debug mode on.
    -p --path PATH      Presentation directory [default: ./].
    -f --file FILE      Reveal.js tar.gz file.
    -h --help           Show this help.

'''

import os
import shutil
import tarfile
import zipfile

from docopt import docopt

from flask_reveal.app import create_app


def start(path, debug):
    if os.path.isdir(path):
        app = create_app(path)

        app.run(debug=debug)
    else:
        print('This is not a valid directory')


def move_and_replace(src, dst):
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)

    for src_dir, dirs, files in os.walk(src):
        dst_dir = src_dir.replace(src, dst)

        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)

        for file in files:
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_dir, file)

            if os.path.exists(dst_file):
                os.remove(dst_file)

            shutil.move(src_file, dst_dir)

    shutil.rmtree(src)


def install_reveal_from_file(file):
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