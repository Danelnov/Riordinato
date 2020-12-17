from shutil import move
import os
import re

# TODO: use pathlib

class Organize():
    """
    Create prefixes and use them to sort files in different folders.

    Attributes
    ----------
    prefixes: list
        list containing prefixes name and destination place.
    path: str
        The folder location where the files to be moved are located.
    files: list
        The files found in the path.

    Methods
    -------
    moveSpecificFiles(prefix, destination)
        Move files with a specific prefix.
    MoveFiles(specific=None)
        Move all files that are in the path.
    getFiles()
        Get the files that are in the path attribute.
    getFilesWP(prefix)
        Get files with prefixes.

    Examples
    --------
    >>> prefixes = [('python', '/home/user/documents/python')]
    >>> path = "/home/user/desktop/python"
    >>> a = Organize(prefixes, path)

    """

    def __init__(self, prefixes: list, path: str):
        """
        Parameters
        ----------
        prefixes: list
            list containing prefixes name and destination place.
        path: str
            The folder location where the files to be moved are located.
        files: list
            The files found in the path.
        """
        self.prefixes = prefixes
        self.path = path
        self.files = self.getFiles()    # get files from path

    def moveSpecificFiles(self, prefix: str, destination: str):
        """Move files with a specific prefix.

        Parameters
        ----------
        prefix: str
            The prefix that the files must contain.
        destination: str
            The directory where files containing the prefix will be moved.
        """

        # Place the program within the address given by the path attribute
        os.chdir(self.path)

        # Generates a list of files containing the prefix
        files = self.getFilesWP(prefix)

        # Move files to destination
        for aprefix in self.prefixes:
            if aprefix[0] == prefix:  # Check if prefix are in self.prefixes
                for file in files:
                    move(file, destination)
                break

    def moveFiles(self, specific: str = None):
        """Move all files that are in the path

        Parameters
        ----------
        specific: str, optional
            Move only files containing this prefix (default is None)
        """

        # Move each file
        for prefix in self.prefixes:
            if specific == None:
                destination = prefix[1]
                self.moveSpecificFiles(prefix[0], destination)
            else:
                if prefix[0] == specific:  # Check if specific are in self.prefixes
                    destination = prefix[1]
                    self.moveSpecificFiles(prefix[0], destination)
                    break

    def getFiles(self) -> list:
        """Get the files that are in the path attribute.

        Return
        ------
        list        
            All the files that are on the path, excluding the folders.
        """
        path = self.path

        # Get the files
        with os.scandir(path) as files:
            files = [afile.name for afile in files if afile.is_file()]

        return files

    def getFilesWP(self, prefix: str) -> list:
        """Get files with prefixes

        get the files that have the prefix through a regular expression

        Parameters
        ----------
        prefix: str
            Prefix that will be used to filter the files that contain it.

        Return
        ------
        list
            All files containing the prefix.

        """
        regex = rf"^{prefix}(...|\w+)\B.+"  # regular expression

        # filter files that have the prefix
        files = list(filter(lambda afile: re.findall(
            regex, afile, re.IGNORECASE), self.files))

        return files

    def __str__(self):
        return self.prefixes
