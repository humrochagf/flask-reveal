# -*- coding: utf-8 -*-

import os
import tempfile
import unittest

from flask import current_app
from flask_reveal.app import FlaskReveal
from flask_reveal.blueprints.reveal import reveal_blueprint
from flask_reveal.config import REVEAL_CONFIG, REVEAL_META

try:
    # Python 3
    FileNotFoundError
except NameError:
    # Python 2
    FileNotFoundError = IOError


class BaseAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = FlaskReveal('flask_reveal')

        self.app.config['TESTING'] = True

        fd, self.config = tempfile.mkstemp('.py')

        os.close(fd)

    def tearDown(self):
        os.remove(self.config)

    def test_start_invalid_config(self):
        self.assertRaises(FileNotFoundError,
                          self.app.start,
                          '', '', 'invalid_file')

    def test_current_app(self):
        with self.app.app_context():
            self.assertEqual(current_app.name, 'flask_reveal')

    def test_blueprint_loading(self):
        with self.app.app_context():
            self.assertDictEqual(current_app.blueprints,
                                 {'reveal': reveal_blueprint})

    def test_default_config_loading(self):
        with self.app.app_context():
            self.assertDictEqual(current_app.config['REVEAL_META'],
                                 REVEAL_META)
            self.assertDictEqual(current_app.config['REVEAL_CONFIG'],
                                 REVEAL_CONFIG)

    def test_user_config_loading(self):
        with open(self.config, 'w') as config:
            config.write('TEST_VAR = "TEST"')

        self.app.load_user_config('', '', self.config)

        with self.app.app_context():
            self.assertEqual(current_app.config['TEST_VAR'], 'TEST')

    def test_user_config_loading_invalid_config_file(self):
        self.assertRaises(FileNotFoundError,
                          self.app.load_user_config,
                          '', '', 'invalid_file')
