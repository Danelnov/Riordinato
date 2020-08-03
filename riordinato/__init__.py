from shutil import move
from os import chdir, listdir, scandir, is_file
import re

__version__ = '0.2.1'


class Organize():
    def __init__(self, prefixes, dirLocation):
        """
        prefixes = [(<prefix>, <Destination>), 
                    (<prefix>, <Destination>),...]

        dirLocation = /home/user/...
        """
        self.prefixes = prefixes
        self.dirLocation = dirLocation

    def __get_files(self):
        """get only files from directory"""
        with scandir(self.dirLocation) as files:
            files = [afile.name for afile in files if files.is_file()]

        return files
    
    def __get_files_wp(self, prefix, files):
        """get the files that have the prefix through a regular expression"""
        regex = "^{}(...|\w+)\B.+".format(prefix)
        files = [afile for afile in files if re.finditer(regex, afile, re.IGNORECASE)]
        return files

    def organize_specific_files(self, prefix):
        """move files with a specific prefix"""
        chdir(self.dirLocation)

        files = self.__get_files()
        files = self.__get_files_wp(prefix, files)

        for prefix in self.prefixes:
            if prefix == prefix[0]:
                for afile in files:
                    move(afile, prefix[1])
                break

    def organize_all(self):
        chdir(self.dirLocation)

        files = self.__get_files()

        for prefix in self.prefixes:
            pfiles = self.__get_files_wp(prefix[0], files)
            for afile in pfiles:
                move(afile, prefix[1])

    def __str__(self):
        return self.prefixes
