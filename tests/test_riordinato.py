from riordinato.files import Organize
import unittest
import os
import re


class TestFiles(unittest.TestCase):

    dir = "/home/daniel/Escritorio/test"
    with os.scandir(dir) as files:
        files = [afile.name for afile in files if afile.is_file()]

    def test_get_files(self):

        order = Organize("", self.dir).get_files()
        self.assertEqual(order, self.files)

    def test_get_fileswp(self):
        order = Organize("", self.dir).get_files_wp("mate", self.files)
        result = ['matehola.txt', 'matenose2.txt', 'matenose.txt', 'mateotra.txt']
        self.assertEqual(order, result)


if __name__ == "__main__":
    unittest.main()
