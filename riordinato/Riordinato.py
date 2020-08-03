from shutil import move
from os import chdir, listdir, scandir


class Organize():
    def __init__(self, prefixes, dirLocation):
        """
        prefixes = [(<prefix>, <Destination>), 
                    (<prefix>, <Destination>),...]

        dirLocation = /home/user/...
        """
        self.prefixes = prefixes
        self.dirLocation = dirLocation

    def __scan_files(self):
        with scandir(self.dirLocation) as files:
            files = [afile.name for afile in files if files.is_file()]

        return files

    def organize_specific_files(self, prefix):
        """move files with a specific prefix"""
        chdir(self.dirLocation)

        files = self.__scan_files

        for i in range(len(self.prefixes)):
            if prefix == self.prefixes[i][0]:
                for afile in files:
                    if prefix in afile:
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
                if self.prefixes[i][0] in afile:
                    move(afile, self.prefixes[i][1])
                    break

    def __str__(self):
        return self.prefixes
