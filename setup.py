#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''

# package variables
package = 'flask_reveal'
requirements = [
    'Flask>=0.12',
]
test_requirements = [
    'mock==2.0.0'
]

# dynamic package info
init_py = open(os.path.join(package, '__init__.py')).read()
version = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
author = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)
email = re.search(
    "^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='flask-reveal',
    version=version,
    description='Make reveal.js presentations with Flask',
    long_description=readme,
    author=author,
    author_email=email,
    url='https://github.com/humrochagf/flask-reveal',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
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
    tests_require=test_requirements
)
