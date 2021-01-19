"""test exceptions"""
import pytest

from riordinato import Riordinato
from riordinato import Prefix
from riordinato.exceptions import EmptyPrefixError
from riordinato.exceptions import InvalidPrefixError


# Test Prefix exception
@pytest.mark.parametrize("name, destination, expected", [
    ("", "directory", EmptyPrefixError),
    (".", "directory", InvalidPrefixError),
    (4, "directory", TypeError),
    ("prefix", "file.txt", NotADirectoryError),
    ("prefix", "python", FileNotFoundError),
])
def test_prefix_class_exceptions(tmp_path, prefix, name, destination, expected):
    with pytest.raises(expected):
        prefix[name] = tmp_path /destination


@pytest.mark.parametrize("path, expected", [
    ("file.txt", NotADirectoryError),
    ("python", FileNotFoundError),
])
def test_path_exception(tmp_path, light_riordinato, path, expected):
    with pytest.raises(expected):
        light_riordinato.path = tmp_path / path
