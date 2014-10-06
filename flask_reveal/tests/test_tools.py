# -*- coding: utf-8 -*-
import os
import shutil
import unittest
import tempfile

from flask_reveal.tools.helpers import move_and_replace


class ToolsTestCase(unittest.TestCase):

    def setUp(self):
        self.source = tempfile.mkdtemp()
        self.dest = tempfile.mkdtemp()
        self.file_to_replace_on_source = os.path.join(self.source, 'replace.txt')
        self.file_to_replace_on_dest = os.path.join(self.dest, 'replace.txt')
        fd, self.file_to_move = tempfile.mkstemp('.txt', dir=self.source)

        os.close(fd)

        with open(self.file_to_replace_on_source, 'w') as f_source, open(self.file_to_replace_on_dest, 'w') as f_dest:
            f_source.write('source')
            f_dest.write('dest')

    def tearDown(self):
        shutil.rmtree(self.dest)

    def test_helper_move_and_replace(self):
        move_and_replace(self.source, self.dest)

        with open(self.file_to_replace_on_dest, 'r') as f:
            file_content = f.read()

        moved_file = os.path.join(self.dest, os.path.basename(self.file_to_move))

        # The moved directory should not exist because it was moved
        self.assertFalse(os.path.exists(self.source))
        # The replaced file should contain the data from the source file
        self.assertEqual(file_content, 'source')
        # The moved file from source should exist on destination directory
        self.assertTrue(os.path.isfile(moved_file))
