from riordinato.files import Organize
import unittest
import os


class TestFiles(unittest.TestCase):
    
    def test_get_files(self):
        dir = "/home/daniel/Escritorio/test"
        with os.scandir(dir) as files:
            files = [afile.name for afile in files if afile.is_file()]
        
        order = Organize("", dir).get_files()
        self.assertEqual(order, files)
        
if __name__ == "__main__":
    unittest.main()
