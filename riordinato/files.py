import re
import os
from shutil import move
from pathlib import Path
from typing import Optional
from typing import Union

from riordinato.exceptions import EmptyPrefixError
from riordinato.exceptions import InvalidPrefixError


class Prefix(dict):
    INVALID_PREFIXES = ["."]

    def __setitem__(self, prefix: str, destination: Union[str, Path]):
        # get absolute path of name
        destination = Path(destination).absolute()

        # check if the path is correct
        if not destination.exists():
            raise FileNotFoundError(
                "This folder does not exist: '{}'".format(destination))
        elif destination.is_file():
            raise NotADirectoryError(
                "Not a directory: '{}'".format(destination))

        # check prefix
        if not prefix:
            raise EmptyPrefixError(prefix)
        else:
            if type(prefix) != str:
                raise TypeError(
                    f"'{prefix}' is a '{type(prefix)}' it should be a string")
            elif prefix in self.INVALID_PREFIXES:
                raise InvalidPrefixError(prefix)

        return dict.__setitem__(self, prefix, destination)


class Riordinato:
    """Create prefixes and use them to sort files in different folders"""

    def __init__(self, path: str):
        """
        Parameters
        ----------
        prefixes : Dict[Prefix, destination]
            dict containing prefixes name and destination place.
        path : str
            The folder location where the files to be moved are located.
        files : list
            The files found in the path.
        """
        self.__path = Path(path).absolute()
        self.files = self.getfiles()    # get files from path
        self.prefixes: dict = Prefix()

    @property
    def path(self):
        return Path(self.__path).absolute()

    @path.setter
    def path(self, new):
        self.__path = Path(new).absolute()

    def _moveSpecificFiles(self, prefix: str, destination: str):
        """Move files with a specific prefix.

        Parameters
        ----------
        prefix : str
            The prefix that the files must contain.
        destination : str
            The directory where files containing the prefix will be moved.
        """

        # Place the program within the address given by the path attribute
        os.chdir(self.__path)

        # Generates a list of files containing the prefix
        files = self.getfilesWP(prefix)

        # Move files to destination
        for file in files:
            move(file, destination)

        self.files = self.getfiles()    # Update file list

    def movefiles(self, specific: Optional[Union[str, list]] = None,
                  ignore: Optional[Union[str, list]] = None):
        """Move all files that are in the path

        Parameters
        ----------
        specific : [str, list], optional
            Move only files containing this prefix (default is None)
        ignore : [str, list], optional
            Prefixes that are ignored (default is None)

        Examples
        --------

        Move all file that have a prefix.

        >>> Riordinato.moveFiles()

        Move all files except those with the math prefix.

        >>> Riordinato.moveFiles(ignore='math')

        Move only files that have prefixes that are in the list.

        >>> Riordinato.moveFiles(specific=['math', 'python', 'scinc e'])
        """
        prefixes = self.prefixes.items()

        if specific:
            # Convert str to list
            specific = [specific] if type(specific) == str else specific
            # Create a list with only the prefixes that are specific
            prefixes = filter(
                lambda prefix: prefix[0] in specific, prefixes)

        if ignore:
            # Convert str to list
            ignore = [ignore] if type(ignore) == str else ignore
            # Create a list of prefixes avoiding the ignored ones
            prefixes = filter(
                lambda prefix: prefix[0] not in ignore, prefixes)

        # Move each file
        for prefix, destination in prefixes:
            self.checkdir(self.path)
            self.checkdir(destination)
            self._moveSpecificFiles(prefix, destination)

    def getfiles(self) -> list:
        """Get the files that are in the path attribute.

        Return
        ------
        list        
            All the files that are on the path, excluding the folders.
        """
        files = self.__path.iterdir()

        # Get the files
        files = [file.name for file in files if file.is_file()]

        return files

    def getfilesWP(self, prefix: str) -> list:
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
        files = list(filter(lambda afile: re.findall(
            regex, afile, re.IGNORECASE), self.files))

        return files

    def checkdir(self, path):
        # check path
        if not path.exists():
            raise FileNotFoundError(
                "This folder does not exist: '{}'".format(path))
        elif path.is_file():
            raise NotADirectoryError(
                "Not a directory: '{}'".format(path))
