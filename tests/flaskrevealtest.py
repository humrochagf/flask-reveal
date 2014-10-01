# -*- coding: utf-8 -*-
import os
from os import fdopen
import shutil
import unittest
import tempfile

from flask_reveal.app import FlaskReveal
from flask_reveal.blueprints.utils import load_markdown_slides


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
        with self.app.get('/') as response:
            self.assertEqual(response.status, '200 OK')

    def test_get_img(self):
        with self.app.get('/img/python.png') as response:
            self.assertEqual(response.status, '200 OK')

    def test_slide_loading(self):
        directory = tempfile.mkdtemp()
        fd, file = tempfile.mkstemp('.md', dir=directory)
        with fdopen(fd, 'w') as f:
            f.write('test')

        slides = load_markdown_slides(directory)

        self.assertEqual(slides, ['test',])

        shutil.rmtree(directory)


if __name__ == '__main__':
    unittest.main()
