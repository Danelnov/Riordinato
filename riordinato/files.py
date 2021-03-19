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
        """special method to return the value of destination turning 
        it into an absolute path
        
        Parameters
        ----------
        prefix: str
            The dictionary key that fulfills the function as a prefix
        destination: str or a Path instance
            The value of the key, receives a string and transforms it into an absolute path
        """
        
        # get absolute path of name
        destination = Path(destination).absolute()

        # check if the path is correct
        if not destination.exists():
            raise FileNotFoundError(
                f"This folder does not exist: '{destination}'")
        elif destination.is_file():
            raise NotADirectoryError(
                f"Not a directory: '{destination}'")

        # check prefix
        if not prefix:
            raise EmptyPrefixError(prefix)
        else:
            if not isinstance(prefix, str):
                raise KeyError(
                    f"{prefix} is an invalid prefix, it should be a string")
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
        absolutepath = Path(new).absolute()
        
        if not absolutepath.exists():
            raise FileNotFoundError(
                "This folder does not exist: '{}'".format(absolutepath))
        elif absolutepath.is_file():
            raise NotADirectoryError(
                "Not a directory: '{}'".format(absolutepath))
            
        self.__path = absolutepath

    def _moveSpecificFiles(self, prefix: str, destination: str):
        """Move files with a specific prefix.

        Parameters
        ----------
        prefix : str
            The prefix that the files must contain.
        destination : str
            The directory where files containing the prefix will be moved.
        """
        self.files = self.getfiles()    # Update file list
        
        os.chdir(self.__path)
        files = self.getfilesWP(prefix)

        for file in files:
            move(file, destination)

        self.files = self.getfiles()   

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

        >>> Riordinato.movefiles()

        Move all files except those with the math prefix.

        >>> Riordinato.movefiles(ignore='math')

        Move only files that have prefixes that are in the list.

        >>> Riordinato.movefiles(specific=['math', 'python', 'scince'])
        """
        prefixes = self.prefixes.items()
        str_to_l = lambda x: [x] if isinstance(x, str) else x

        if specific:
            # Convert str to list
            specific = str_to_l(specific)
            # Create a list with only the prefixes that are specific
            prefixes = filter(
                lambda prefix: prefix[0] in specific, prefixes)

        if ignore:
            # Convert str to list
            ignore = str_to_l(ignore)
            # Create a list of prefixes avoiding the ignored ones
            prefixes = filter(
                lambda prefix: prefix[0] not in ignore, prefixes)

        for prefix, destination in prefixes:
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
