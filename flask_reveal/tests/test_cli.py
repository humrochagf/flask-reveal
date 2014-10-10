# -*- coding: utf-8 -*-
import os
import shutil
import unittest
import tempfile

from flask_reveal.tools.cli import CLI
from flask_reveal.tools.commands import load_subcomand, start, installreveal, mkpresentation


class CLITestCase(unittest.TestCase):

    def setUp(self):
        self.cli = CLI()

    def test_available_subcomands(self):
        subcommands = sorted(['start', 'installreveal', 'mkpresentation'])

        self.assertListEqual(subcommands, sorted(self.cli.subcommands))

    def test_parse_subcommand(self):
        self.cli.parse_known_args(['start', ])

        self.assertEqual(self.cli.subcommand, 'start')

    def test_load_subcommand(self):
        subcommand = load_subcomand('start')

        self.assertIsInstance(subcommand, start.Start)


class CommandsTestCase(unittest.TestCase):

    def mk_project_structure(self):
        source = tempfile.mkdtemp()

        os.mkdir(os.path.join(source, 'img'))

        with open(os.path.join(source, 'config.py'), 'w') as f:
            f.write('# test')

        return source

    def setUp(self):
        self.start = start.Start()
        self.install_reveal = installreveal.InstallReveal()
        self.mk_presentation = mkpresentation.MkPresentation()
        self.project_dir = self.mk_project_structure()

    def tearDown(self):
        shutil.rmtree(self.project_dir)

    def test_start_parse_args(self):
        self.start.parse_args([self.project_dir, ])

        self.assertEqual(self.start.path, self.project_dir)
        self.assertEqual(self.start.media,
                         os.path.join(self.project_dir, 'img'))
        self.assertEqual(self.start.config,
                         os.path.join(self.project_dir, 'config.py'))

    def test_start_parse_args_invalid_img_root(self):
        self.assertRaises(NotADirectoryError, self.start.parse_args,
                          [self.project_dir, '-m invalid_media'])

    def test_start_parse_args_invalid_root(self):
        self.assertRaises(NotADirectoryError, self.start.parse_args,
                          ['invalid_root', ])

    def test_install_reveal_parse_args(self):
        self.install_reveal.parse_args([])

        self.assertEqual(self.install_reveal.path, None)
        self.assertEqual(self.install_reveal.url,
                         'https://github.com/hakimel/reveal.js/' +
                         'archive/2.6.2.tar.gz')

    def test_mk_presentation_parse_args(self):
        self.mk_presentation.parse_args([])

        self.assertEqual(self.mk_presentation.path, 'my_presentation')

    def test_mk_presentation_run_directory_exists(self):
        self.assertRaises(FileExistsError, self.mk_presentation.run,
                          [self.project_dir, ])
