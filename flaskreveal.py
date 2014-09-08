#!/usr/bin python
# -*- coding: utf-8 -*-
"""flask-reveal

Usage:
    flaskreveal start [-d | --debug]
    flaskreveal start [-d | --debug] PATH
    flaskreveal mkpresentation
    flaskreveal mkpresentation NAME
    flaskreveal installreveal
    flaskreveal installreveal -f FILE
    flaskreveal installreveal -u URL
    flaskreveal -h | --help

Options:
    -d --debug              Start flask with debug mode on.
    -f FILE --file=FILE     Reveal.js .tar.gz or .zip release file.
    -u URL --url=URL        Url of reveal.js .tar.gz or .zip release file.
    -h --help               Show this help.

"""

from docopt import docopt

from flask_reveal.manager import start, make_presentation, install_from_web, install_reveal_from_file


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['start']:
        path, debug = arguments['PATH'], arguments['--debug']

        if path:
            start(path, debug)
        else:
            start('./', debug)

    elif arguments['mkpresentation']:
        name = arguments['NAME']

        if name:
            make_presentation(name)
        else:
            make_presentation()

    elif arguments['installreveal']:
        file, url = arguments['--file'], arguments['--url']

        if file:
            print('Installing reveal.js from file...')
            install_reveal_from_file(file)
        elif url:
            print('Installing reveal.js from web...')
            install_from_web(url)
        else:
            print('Installing reveal.js from default url...')
            install_from_web('https://github.com/hakimel/reveal.js/archive/2.6.2.tar.gz')
