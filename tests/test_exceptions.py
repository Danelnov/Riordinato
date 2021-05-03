"""test exceptions"""
import pytest

from riordinato import Riordinato
from riordinato import Prefix
from riordinato.exceptions import EmptyPrefixError
from riordinato.exceptions import InvalidPrefixError
from shutil import SameFileError


# Test Prefix exception
@pytest.mark.parametrize("name, destination, expected", [
    ("", "directory", EmptyPrefixError),
    (".", "directory", InvalidPrefixError),
    (4, "directory", KeyError),
    ("prefix", "file.txt", NotADirectoryError),
    ("prefix", "python", FileNotFoundError),
])
def test_prefix_class_exceptions(tmp_path, prefix, name, destination, expected):
    """Test for exceptions of the prefix class.

    When a prefix is invalid there is an error, one of them is to 
    put invalid prefixes like "." which generates that all files 
    are read, also checks the path, ensures that it is not a file 
    and that the directory exists.
    """
    with pytest.raises(expected):
        prefix[name] = tmp_path / destination


@pytest.mark.parametrize("path, expected", [
    ("file.txt", NotADirectoryError),
    ("python", FileNotFoundError),
])
def test_path_exception(tmp_path, light_riordinato, path, expected):
    """Test that checks the operation of exceptions of the path attribute
    
    These exceptions occur when trying to modify the path attribute.
    For example when it is changed by a file and not a directory.
    """
    with pytest.raises(expected):
        light_riordinato.path = tmp_path / path


def test_same_file_exception(tmp_path, light_riordinato):
    """Test that checks the exception when there are two files with the same name"""
    with pytest.raises(SameFileError):
        light_riordinato.check_files(tmp_path / "directory")
