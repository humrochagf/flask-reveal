# -*- coding: utf-8 -*-
import unittest

from flask_reveal.tools.cli import CLI


class CLITestCase(unittest.TestCase):

    def setUp(self):
        self.cli = CLI()

    def test_available_subcomands(self):
        subcommands = sorted(['start', 'installreveal', 'mkpresentation'])

        self.assertListEqual(subcommands, sorted(self.cli.subcommands))

    def test_parse_subcommand(self):
        self.cli.parse_known_args(['start',])

        self.assertEqual(self.cli.subcommand, 'start')
