from shutil import move
import os
import re


class Organize():
    def __init__(self, prefixes: list, path: str):
        """
        prefixes = [(<prefix>, <Destination>), 
                    (<prefix>, <Destination>),...]

        path = '/home/user/...'
        """
        self.prefixes = prefixes
        self.path = path
        self.files = self.getFiles()    # get files from path

    def organize_specific_files(self, prefix: str):
        """move files with a specific prefix"""

        # Place the program within the address given by the path attribute
        os.chdir(self.path)

        # Get files that have the prefix
        files = self.getFilesWP(prefix)

        # Move files to path
        for aprefix in self.prefixes:
            if aprefix[0] == prefix: # First check if prefix are in self.prefixes
                for afile in files:
                    move(afile, aprefix[1])
                break

    def MoveFiles(self):
        """move all files that are in the path"""
        
        # Place the program within the address given by the path attribute
        os.chdir(self.path)

        # Move each file
        for prefix in self.prefixes:
            # Generates a list of files containing the prefix
            pfiles = self.getFilesWP(prefix[0]) 
            # If the list is not empty start moving them
            if pfiles:
                for afile in pfiles:
                    move(afile, prefix[1])

    def getFiles(self) -> list:
        """Get the files that are in the path attribute.

        Get all the files that are on the path, excluding the folders 
        and returning only the files.
        """
        path = self.path

        with os.scandir(path) as files:
            files = [afile.name for afile in files if afile.is_file()]

        return files

    def getFilesWP(self, prefix: str) -> list:
        """Get files with prefixes
        
        get the files that have the prefix through a regular expression

        Use the filter function to be able to find within 
        the list the files that contain the assigned prefix.

        Parameters:
        prefix -- prefix to be searched for in the file, it must be a string.

        """
        regex = rf"^{prefix}(...|\w+)\B.+"  # regular expression

        # filter files that have the prefix
        files = list(filter(lambda afile: re.findall(
            regex, afile, re.IGNORECASE), self.files))

        return files

    def __str__(self):
        return self.prefixes
