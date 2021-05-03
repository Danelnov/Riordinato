import pytest
from riordinato import Prefix

def test_absolute_path(tmp_path, prefix):
    """Test that verifies that the path assigned to the prefixes value is an absolute path"""
    prefix['name'] = tmp_path / 'directory'
    assert prefix['name'].is_absolute(), f"{prefix['name']} not is absolute"
