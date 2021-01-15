"""test exceptions"""
import pytest

from riordinato import Riordinato
from riordinato import Prefix
from riordinato.exceptions import EmptyPrefixError
from riordinato.exceptions import InvalidPrefixError
from riordinato.exceptions import TypePrefixError

from .conftest import create

# Test Prefix exception
@pytest.mark.parametrize("name, destination, expected", [
    ("", "directoy", EmptyPrefixError),
    (".", "directoy", InvalidPrefixError),
    (4, "directoy", TypePrefixError),
    ("prefix", "file.txt", NotADirectoryError),
    ("prefix", "python", FileNotFoundError),
])
def test_prefix_class(tmp_path, name, destination, expected):
    # Create files and dirs in a temporal dir
    create(tmp_path, ["file.txt"], ["directoy"])
        
    with pytest.raises(expected):
        Prefix(name, tmp_path / destination).checkPrefix()    
