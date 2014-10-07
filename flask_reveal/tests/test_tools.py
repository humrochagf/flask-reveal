# -*- coding: utf-8 -*-
import os
import tarfile
import shutil
import unittest
import tempfile

from flask_reveal.tools.helpers import move_and_replace, extract_file


class ToolsTestCase(unittest.TestCase):

    def make_src(self, base):
        source = tempfile.mkdtemp(dir=base)
        file_to_replace_on_source = os.path.join(source, 'replace.txt')
        fd, file_to_move = tempfile.mkstemp('.txt', dir=source)

        os.close(fd)

        with open(file_to_replace_on_source, 'w') as f_source:
            f_source.write('source')

        return source

    def make_dst(self, base):
        destination = tempfile.mkdtemp(dir=base)
        file_to_replace_on_dest = os.path.join(destination, 'replace.txt')

        with open(file_to_replace_on_dest, 'w') as f_dest:
            f_dest.write('dest')

        return destination

    def make_tar(self, content, base):
        fd, tar = tempfile.mkstemp('.tar.gz', dir=base)

        os.close(fd)

        with tarfile.open(tar, 'w:gz') as t:
            t.add(content, arcname='tarfolder')

        return tar

    def setUp(self):
        self.base = tempfile.mkdtemp()
        self.source = self.make_src(self.base)
        self.destination = self.make_dst(self.base)
        self.tar = self.make_tar(self.source, self.base)

    def tearDown(self):
        shutil.rmtree(self.base)

    def test_helper_move_and_replace(self):
        src_files = sorted(os.listdir(self.source))

        move_and_replace(self.source, self.destination)

        dst_files = sorted(os.listdir(self.destination))

        with open(os.path.join(self.destination, 'replace.txt'), 'r') as f:
            file_content = f.read()

        # The moved directory should not exist because it was moved
        self.assertFalse(os.path.exists(self.source))
        # The replaced file should contain the data from the source file
        self.assertEqual(file_content, 'source')
        # The moved files from source should be equal to the files on destination directory
        self.assertEqual(src_files, dst_files)

    def test_extract_file(self):
        src_files = sorted(os.listdir(self.source))

        extracted = extract_file(self.tar, self.base)

        extracted_files = sorted(os.listdir(extracted))

        self.assertEqual(extracted_files, src_files)

    def test_extract_file_on_non_file(self):
        self.assertRaises(TypeError, extract_file, self.base)

    def test_extract_file_on_non_tar_or_zip(self):
        files = os.listdir(self.destination)

        self.assertRaises(TypeError, extract_file, files[0])
