# -*- coding: utf-8 -*-
import os
import unittest

from flask_reveal.app import FlaskReveal


class FlaskRevealTestCase(unittest.TestCase):
    def create_app(self):
        presentation_root = os.path.abspath(os.path.join(os.path.basename(__file__), '../example_slides'))
        app_config = FlaskReveal('flask_reveal')
        app_config.config['PRESENTATION_ROOT'] = presentation_root
        app_config.config['MEDIA_ROOT'] = os.path.join(presentation_root, 'img')
        app_config.config['TESTING'] = True

        return app_config.test_client()

    def setUp(self):
        self.app = self.create_app()

    def test_presentation_view_status(self):
        response = self.app.get('/')

        self.assertEqual(response.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
