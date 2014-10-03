# -*- coding: utf-8 -*-
import os
import shutil
import unittest
import tempfile

from flask import current_app

from flask_reveal.app import FlaskReveal
from flask_reveal.config import REVEAL_CONFIG, REVEAL_META
from flask_reveal.blueprints.utils import load_markdown_slides
from flask_reveal.blueprints.reveal import reveal_blueprint


class FlaskRevealTestCase(unittest.TestCase):
    slides = ['Slide1', 'Slide2', 'Slide3']

    def create_presentation_structure(self, slides=None):
        presentation_root = tempfile.mkdtemp()
        media_root = tempfile.mkdtemp()

        fd, img_file = tempfile.mkstemp('.jpg', dir=media_root)

        os.close(fd)

        with open(os.path.join(presentation_root, 'config.py'), 'w') as config_file:
            config_file.write('# test')

        for index, slide in enumerate(slides):
            fd, _ = tempfile.mkstemp('.md', str(index), presentation_root)
            with os.fdopen(fd, 'w') as file:
                file.write(slide)

        return presentation_root, media_root, os.path.basename(img_file)

    def create_test_client(self, presentation_root, media_root):
        app = FlaskReveal('flask_reveal')

        app.load_user_config(presentation_root, media_root)
        app.config['TESTING'] = True

        return app.test_client()

    def setUp(self):
        self.app = FlaskReveal('flask_reveal')

        self.app.config['TESTING'] = True

        self.presentation_root, self.media_root, self.img_file = self.create_presentation_structure(self.slides)

    def tearDown(self):
        shutil.rmtree(self.presentation_root)

    def test_current_app(self):
        with self.app.app_context():
            self.assertEqual(current_app.name, 'flask_reveal')

    def test_blueprint_loading(self):
        with self.app.app_context():
            self.assertDictEqual(current_app.blueprints, {'reveal': reveal_blueprint})

    def test_default_config_loading(self):
        with self.app.app_context():
            self.assertDictEqual(current_app.config['REVEAL_META'], REVEAL_META)
            self.assertDictEqual(current_app.config['REVEAL_CONFIG'], REVEAL_CONFIG)

    def test_presentation_view_status(self):
        client = self.create_test_client(self.presentation_root, self.media_root)

        with client.get('/') as response:
            self.assertEqual(response.status, '200 OK')

    def test_get_img_view_status(self):
        client = self.create_test_client(self.presentation_root, self.media_root)

        with client.get('/img/{0}'.format(self.img_file)) as response:
            self.assertEqual(response.status, '200 OK')

    def test_load_markdown_slides(self):
        slides = load_markdown_slides(self.presentation_root)

        self.assertEqual(slides, self.slides)
