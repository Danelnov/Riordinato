from typing import Any


class RiordinatoError(Exception):
    """Riordinato base Error"""


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
