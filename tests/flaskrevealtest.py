# -*- coding: utf-8 -*-
import os
import unittest

from flask_reveal.app import FlaskReveal


class FlaskRevealTestCase(unittest.TestCase):
    def setUp(self):
        app_config = FlaskReveal('flask_reveal')

        app_config.config['PRESENTATION_ROOT'] = os.path.abspath(os.path.join(__file__, '../exaple_slides'))
        app_config.config['MEDIA_ROOT'] = os.path.join(app_config.config['PRESENTATION_ROOT'], 'img')
        app_config.config['TESTING'] = True

        self.app = app_config.test_client()

    def test_presentation_view_status(self):
        response = self.app.get('/')

        self.assertEqual(response.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
