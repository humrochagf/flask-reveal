#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''flask-reveal setup file'''

import os
import re

from setuptools import find_packages, setup

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

# package variables
PACKAGE = 'flask_reveal'
REQUIREMENTS = [
    'Flask>=0.12',
]
TEST_REQUIREMENTS = [
    'coverage==4.4.1',
    'mock==2.0.0',
    'nose==1.3.7',
    'pylint-flask==0.5',
    'pylint==1.7.1',
]

# dynamic package info
with open(os.path.join(PACKAGE, '__init__.py')) as init_file:
    INIT = init_file.read()
VERSION = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)
AUTHOR = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)
EMAIL = re.search(
    "^__email__ = ['\"]([^'\"]+)['\"]", INIT, re.MULTILINE).group(1)

setup(
    name='flask-reveal',
    version=VERSION,
    description='Make reveal.js presentations with Flask',
    long_description=README,
    long_description_content_type='text/markdown; charset=UTF-8',
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/humrochagf/flask-reveal',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points=dict(
        console_scripts=['flaskreveal=flask_reveal.tools.cli:cli_execute']),
    platforms='any',
    keywords=['flask', 'reveal.js', 'presentation'],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS
)
