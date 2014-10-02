# -*- coding: utf-8 -*-
import os
from os import fdopen
import shutil
import unittest
import tempfile

from flask_reveal.app import FlaskReveal
from flask_reveal.blueprints.utils import load_markdown_slides


class FlaskRevealTestCase(unittest.TestCase):
    slides = ['Slide1', 'Slide2', 'Slide3']

    def create_presentation_structure(self, slides=None):
        presentation_root = tempfile.mkdtemp()
        media_root = tempfile.mkdtemp()
        fd, img_file = tempfile.mkstemp('.jpg', dir=media_root)

        os.close(fd)

        for index, slide in enumerate(slides):
            fd, _ = tempfile.mkstemp('.md', str(index), presentation_root)
            with fdopen(fd, 'w') as file:
                file.write(slide)

        return presentation_root, media_root, os.path.basename(img_file)

    def create_app(self, presentation_root, media_root):
        app_config = FlaskReveal('flask_reveal')
        app_config.config['PRESENTATION_ROOT'] = presentation_root
        app_config.config['MEDIA_ROOT'] = media_root
        app_config.config['TESTING'] = True

        return app_config.test_client()

    def setUp(self):
        self.presentation_root, self.media_root, self.img_file = self.create_presentation_structure(self.slides)
        self.app = self.create_app(self.presentation_root, self.media_root)

    def tearDown(self):
        shutil.rmtree(self.presentation_root)

    def test_presentation_view_status(self):
        with self.app.get('/') as response:
            self.assertEqual(response.status, '200 OK')

    def test_get_img_view_status(self):
        with self.app.get('/img/{0}'.format(self.img_file)) as response:
            self.assertEqual(response.status, '200 OK')

    def test_load_markdown_slides(self):
        slides = load_markdown_slides(self.presentation_root)

        self.assertEqual(slides, self.slides)


if __name__ == '__main__':
    unittest.main()
