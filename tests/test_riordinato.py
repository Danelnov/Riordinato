from riordinato.files import Organize
import unittest
import os
import re


class TestFiles(unittest.TestCase):

    dir = "/home/daniel/Escritorio/test"
    files = ['sldkafj.txt', 'script.py', 'ciencias_asco.txt', 'cienciasmas.txt',
             'matejajas.txt', 'mate.txt', 'wofew.txt', 'a', 'slkdCiencias.py',
             'Matesdfl.py', 'ciencias.txt', 'ciencias_ciencias.txt',
             'ciencias_mierdad.txt', 'noseMate.txt', 'dfow.txt', 'regular.py']

    def test_get_files(self):

        order = Organize("", self.dir)
        self.assertEqual(order.files, self.files)

    def test_get_fileswp(self):
        order = Organize("", self.dir).get_files_wp("mate", self.files)
        result = ['matejajas.txt', 'mate.txt', 'Matesdfl.py']
        self.assertEqual(order, result)


if __name__ == "__main__":
    unittest.main()
