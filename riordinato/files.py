from shutil import move
import os
import re


class Organize():
    def __init__(self, prefixes, dirLocation):
        """
        prefixes = [(<prefix>, <Destination>), 
                    (<prefix>, <Destination>),...]

        dirLocation = /home/user/...
        """
        self.prefixes = prefixes
        self.dirLocation = dirLocation
        self.files = self.get_files()
        

    def get_files(self):
        """get only files from directory"""
        dir = self.dirLocation
        with os.scandir(dir) as files:
            files = [afile.name for afile in files if afile.is_file()]

        return files
    
    def get_files_wp(self, prefix, files):
        """get the files that have the prefix through a regular expression"""
        regex = rf"^{prefix}(...|\w+)\B.+"
        files = [afile for afile in files if re.findall(regex, afile, re.IGNORECASE)]
        return files

    def organize_specific_files(self, prefix):
        """move files with a specific prefix"""
        os.chdir(self.dirLocation)

        files = self.get_files_wp(prefix, self.files)
        
        for aprefix in self.prefixes:
            if aprefix[0] == prefix:
                for afile in files:
                    move(afile, aprefix[1])
                break
                

    def organize_all(self):
        os.chdir(self.dirLocation)

        for prefix in self.prefixes:
            pfiles = self.get_files_wp(prefix[0], self.files)
            if pfiles:
                for afile in pfiles:
                    move(afile, prefix[1])

    def __str__(self):
        return self.prefixes
