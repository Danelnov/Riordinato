from inspect import getfile
from shutil import move
from pathlib import Path
import re
import os


class Prefix:
    def __init__(self, name: str, destination: str):
        """
        Parameters
        ----------
        name : str
            Name of prefix.
        destination : str
            Prefix destination, must be a path.
        """
        self.prefix = name
        self.path = Path(destination)


class Riordinato:
    """
    Create prefixes and use them to sort files in different folders.

    Attributes
    ----------
    prefixes : list
        list containing prefixes name and destination place `prefixes`.
    path : str
        The folder location where the files to be moved are located.
    files : list
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
    >>> prefixes = [('python', '/home/user/documents/python'),
    ...             ('math', '/home/user/documents/math')]
    >>> path = "/home/user/desktop/python"
    >>> a = Riordinato(prefixes, path)

    """

    def __init__(self, prefixes: list, path: str):
        """
        Parameters
        ----------
        prefixes : list
            list containing prefixes name and destination place.
        path : str
            The folder location where the files to be moved are located.
        files : list
            The files found in the path.
        """
        self.prefixes = prefixes
        self.path = Path(path)
        self.files = self.getFiles()    # get files from path

    def moveSpecificFiles(self, prefix: str, destination: str):
        """Move files with a specific prefix.

        Parameters
        ----------
        prefix : str
            The prefix that the files must contain.
        destination : str
            The directory where files containing the prefix will be moved.
        """

        # Place the program within the address given by the path attribute
        os.chdir(self.path)

        # Generates a list of files containing the prefix
        files = self.getFilesWP(prefix)

        # Move files to destination
        for aprefix in self.prefixes:
            if aprefix[0] == prefix:    # Check if prefix are in self.prefixes
                for file in files:
                    move(file, destination)
                break
        
        self.files = self.getFiles()    # Update file list
        
    def moveFiles(self, specific=None, ignore=None):
        """Move all files that are in the path

        Parameters
        ----------
        specific : str, list, optional
            Move only files containing this prefix (default is None)
        ignore : str, list, optional
            Prefixes that are ignored (default is None)

        Examples
        --------
        
        Move all file that have a prefix.

        >>> Riordinato.moveFiles()
        
        Move only files that have math prefix.
        
        >>> Riordinato.moveFiles(specific='math')

        Move all files except those with the math prefix.
        
        >>> Riordinato.moveFiles(ignore='math')
        
        Move only files that have prefixes that are in the list.
        
        >>> Riordinato.moveFiles(specific=['math', 'python', 'scince'])
        """
        prefixes = self.prefixes

        if specific:
            # Convert str to list
            specific = [specific] if type(specific) == str else specific
            # Create a list with only the prefixes that are specific
            prefixes = filter(lambda prefix: prefix[0] in specific, prefixes)
        
        if ignore:
            # Convert str to list
            ignore = [ignore] if type(ignore) == str else ignore
            # Create a list of prefixes avoiding the ignored ones
            prefixes = filter(lambda prefix: prefix[0] not in ignore, prefixes)
        
        # Move each file
        for prefix in prefixes:
                destination = prefix[1]
                self.moveSpecificFiles(prefix[0], destination)

    def getFiles(self) -> list:
        """Get the files that are in the path attribute.

        Return
        ------
        list        
            All the files that are on the path, excluding the folders.
        """
        files = self.path.iterdir()

        # Get the files
        files = [file.name for file in files if file.is_file()]

        return files

    def getFilesWP(self, prefix: str) -> list:
        """Get files with prefixes

        get the files that have the prefix through a regular expression

        Parameters
        ----------
        prefix : str
            Prefix that will be used to filter the files that contain it.

        Return
        ------
        list
            All files containing the prefix.

        """
        regex = rf"^{prefix}(...|\w+)\B.+"  # regular expression

        # filter files that have the prefix
        files = list(filter(lambda afile: re.findall(regex, afile, re.IGNORECASE), self.files))

        return files

    def __str__(self) -> str:
        return self.prefixes
