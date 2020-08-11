from riordinato.files import Organize
import unittest
import os
import re


class TestFiles(unittest.TestCase):

    dir = "/home/daniel/Escritorio/test"
    files = ['matenose.txt', 'sldkafj.txt', 'script.py', 'ciencias_asco.txt', 
             'matehola.txt', 'mateotra.txt', 'cienciasmas.txt', 'wofew.txt',
             'ciencias.txt', 'ciencias_ciencias.txt', 'ciencias_mierdad.txt', 'dfow.txt', 
             'matenose2.txt', 'regular.py']

    def test_get_files(self):

        order = Organize("", self.dir).get_files()
        self.assertEqual(order, self.files)

    def test_get_fileswp(self):
        order = Organize("", self.dir).get_files_wp("mate", self.files)
        result = ['matenose.txt', 'matehola.txt',
                  'mateotra.txt', 'matenose2.txt']
        self.assertEqual(order, result)


if __name__ == "__main__":
    unittest.main()
