# -*- coding: utf-8 -*-
from subprocess import call
from setuptools import setup, find_packages
from setuptools.command.install import install


class CustomInstall(install):
    """
    Include reveal.js installation process
    """
    def run(self):
        install.run(self)
        # calling reveal installation
        call(['flaskreveal', 'installreveal'], cwd=self.install_scripts)


setup(
    name='flask-reveal',
    version='0.1.dev1',
    url='https://github.com/humrochagf/flask-reveal',
    license='MIT',
    author='Humberto Rocha Gonçalves Filho',
    author_email='humrochagf@gmail.com',
    description='Make reveal.js presentations with Flask',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="flask_reveal.tests",
    install_requires=[
        'Flask>=0.10',
    ],
    entry_points=dict(
        console_scripts=['flaskreveal=flask_reveal.tools.cli:cli_execute']),
    cmdclass=dict(install=CustomInstall),
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
