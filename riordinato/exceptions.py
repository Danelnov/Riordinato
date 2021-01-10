from typing import Any


class RiordinatoError(Exception):
    """Riordinato base Error"""


class DirNotExistsError(RiordinatoError):
    """Base dir error"""

    def __init__(self, dir_name: str):
        """
        Parameters:
        -----------
        dir_name: str
            Directory name.
        """
        self.dir_name = dir_name
        super().__init__(self.error_message)

    @property
    def error_message(self):
        return f"{self.dir_name} not exists"


class DirIsFileError(DirNotExistsError):
    """Directory is a file"""

    def __init__(self, dir_name: str):
        self.dir_name = dir_name
        super().__init__(self.dir_name)

    @property
    def error_message(self):
        return f"{self.dir_name} is a file"


class InvalidPrefixError(RiordinatoError):
    """Base invalid prefix erro"""

    def __init__(self, prefix_name: str):
        """
        Parameters:
        -----------
        prefix_name: str
            Name of prefix.
        """
        self.prefix_name = prefix_name
        super().__init__(self.error_message)

    @property
    def error_message(self):
        return f"{self.prefix_name} is a invalid prefix"


class EmptyPrefixError(InvalidPrefixError):
    """Prefix is empty"""

    def __init__(self, prefix_name: str):
        """
        Parameters:
        -----------
        prefix_name: str
            Name of prefix.
        """
        self.prefix_name = prefix_name
        super().__init__(self.prefix_name)

    @property
    def error_message(self):
        return "the prefix must contain some name"


class TypePrefixError(InvalidPrefixError):
    """The prefix is not a string"""
    
    def __inti__(self, prefix_name: Any):
        """
        Parameters:
        -----------
        prefix_name: str
            Name of prefix.
        """
        self.prefix_name = prefix_name
        super().__init__(self.prefix_name)
    
    @property
    def error_message(self):
        return f"{self.prefix_name} is a {type(self.prefix_name)} it should be a string"
