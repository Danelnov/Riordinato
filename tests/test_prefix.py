import pytest
from riordinato import Prefix

def test_absolute_path(tmp_path, prefix):
    prefix['name'] = tmp_path / 'directory'
    assert prefix['name'].is_absolute(), f"{prefix['name']} not is absolute"
