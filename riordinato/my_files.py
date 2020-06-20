from shutil import move
from os import chdir, listdir


class Organize():

    def __init__(self, prefixes, dirLocation):
        """
        prefixes = [(<prefix>, <Destination>), 
                    (<prefix>, <Destination>),...]
        """
        self.prefixes = prefixes
        self.dirLocation = dirLocation

    def organize_specific_files(self, prefix):
        """move files with a specific prefix"""
        chdir(self.dirLocation)
        files = listdir('./')

        for i in range(len(self.prefixes)):
            if prefix == self.prefixes[i][0]:
                for afile in files:
                    if prefix in afile and '.' in afile:
                        move(afile, self.prefixes[i][1])
                        print(afile, "moved")
                    else:
                        print(afile, "It does not move")
                break

    def organize_all(self):
        chdir(self.dirLocation)
        files = listdir('./')

        for afile in files:
            for i in range(len(self.prefixes)):
                if self.prefixes[i][0] in afile and '.' in afile:
                    move(afile, self.prefixes[i][1])
                    break
