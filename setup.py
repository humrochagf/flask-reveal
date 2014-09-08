# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name = 'flask-reveal',
    version = '0.1',
    license = 'MIT',
    description = 'Make reveal.js presentations with Flask',
    author = 'Humberto Rocha Gonçalves Filho',
    author_email = 'humrochagf@gmail.com',
    url = 'https://github.com/humrochagf/flask-reveal',
    keywords = ['flask', 'reveal.js', 'presentation'],
    packages = ['flask_reveal'],
    platforms = 'any',
    scripts = ['flaskreveal.py'],
    classifiers = [
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Text Processing :: Markup :: HTML',
        ]
)