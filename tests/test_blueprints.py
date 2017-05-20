# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
import unittest

from flask_reveal.app import FlaskReveal
from flask_reveal.blueprints.reveal import load_markdown_slide


class BlueprintTestCase(unittest.TestCase):
    slides = 'Slide1\n---\nSlide2\n---\nSlide3'

    def create_presentation_structure(self, slides=None):
        root = tempfile.mkdtemp()
        media = tempfile.mkdtemp()

        fd_cfg, config = tempfile.mkstemp('.py', dir=root)
        fd_img, image = tempfile.mkstemp('.jpg', dir=media)

        os.close(fd_cfg)
        os.close(fd_img)

        fd, presentation_file = tempfile.mkstemp('.md', dir=root)

        with os.fdopen(fd, 'w') as file:
            file.write(slides)

        return dict(presentation_file=presentation_file,
                    root=root,
                    media=media,
                    config=config,
                    image=os.path.basename(image))

    def create_client(self, presentation_file, media_root, config):
        app = FlaskReveal('flask_reveal')

        app.load_user_config(presentation_file, media_root, config)
        app.config['TESTING'] = True

        return app.test_client()

    def setUp(self):
        self.presentation = self.create_presentation_structure(self.slides)

    def tearDown(self):
        shutil.rmtree(self.presentation['root'])

    def test_presentation_view_status(self):
        client = self.create_client(self.presentation['presentation_file'],
                                    self.presentation['media'],
                                    self.presentation['config'])

        with client.get('/') as response:
            self.assertEqual(response.status, '200 OK')

    def test_get_img_view_status(self):
        client = self.create_client(self.presentation['presentation_file'],
                                    self.presentation['media'],
                                    self.presentation['config'])
        url = '/img/{0}'.format(self.presentation['image'])

        with client.get(url) as response:
            self.assertEqual(response.status, '200 OK')

    def test_load_markdown_slide(self):
        slides = load_markdown_slide(self.presentation['presentation_file'],
                                     '---')

        self.assertEqual(slides, ['Slide1\n', '\nSlide2\n', '\nSlide3'])
