# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='flask-reveal',
    version='0.1',
    url='https://github.com/humrochagf/flask-reveal',
    license='MIT',
    author='Humberto Rocha Gonçalves Filho',
    author_email='humrochagf@gmail.com',
    description='Make reveal.js presentations with Flask',
    packages=['flask_reveal', 'flask_reveal.blueprints'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10',
        'docopt>=0.6',
    ],
    scripts=['flaskreveal.py'],
    platforms='any',
    keywords=['flask', 'reveal.js', 'presentation'],
    classifiers=[
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
