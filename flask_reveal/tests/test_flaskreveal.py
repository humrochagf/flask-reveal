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
        root = tempfile.mkdtemp()
        media = tempfile.mkdtemp()

        fd_cfg, config = tempfile.mkstemp('.py', dir=root)
        fd_img, image = tempfile.mkstemp('.jpg', dir=media)

        os.close(fd_cfg)
        os.close(fd_img)

        for index, slide in enumerate(slides):
            fd, _ = tempfile.mkstemp('.md', str(index), root)
            with os.fdopen(fd, 'w') as file:
                file.write(slide)

        return dict(root=root,
                    media=media,
                    config=config,
                    image=os.path.basename(image))

    def create_test_client(self, presentation_root, media_root, config):
        app = FlaskReveal('flask_reveal')

        app.load_user_config(presentation_root, media_root, config)
        app.config['TESTING'] = True

        return app.test_client()

    def setUp(self):
        self.app = FlaskReveal('flask_reveal')

        self.app.config['TESTING'] = True

        self.presentation = self.create_presentation_structure(self.slides)

    def tearDown(self):
        shutil.rmtree(self.presentation['root'])

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

    def test_user_config_loading(self):
        with open(self.presentation['config'], 'w') as config:
            config.write('TEST_VAR = "TEST"')

        self.app.load_user_config('', '', self.presentation['config'])

        with self.app.app_context():
            self.assertEqual(current_app.config['TEST_VAR'], 'TEST')

    def test_presentation_view_status(self):
        client = self.create_test_client(self.presentation['root'],
                                         self.presentation['media'],
                                         self.presentation['config'])

        with client.get('/') as response:
            self.assertEqual(response.status, '200 OK')

    def test_get_img_view_status(self):
        client = self.create_test_client(self.presentation['root'],
                                         self.presentation['media'],
                                         self.presentation['config'])

        with client.get('/img/{0}'.format(self.presentation['image'])) as response:
            self.assertEqual(response.status, '200 OK')

    def test_load_markdown_slides(self):
        slides = load_markdown_slides(self.presentation['root'])

        self.assertEqual(slides, self.slides)
