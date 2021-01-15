"""Tests of the Riordinato class methods"""
from riordinato import Riordinato
import pytest


def get_tmp_files(tmp_path):
    """Get the files from a folder in the temporal path

    Returns only the file name
    """
    # filter files from tmp_path avoiding directories
    tmp_files = list(filter(lambda x: x.is_file(),
                            tmp_path.iterdir()))
    # Create a list of file names
    tmp_files = [file.name for file in tmp_files]

    return tmp_files


@pytest.mark.parametrize("prefix, expected", [
    ("python", ["pythonCourse.txt", "Python_tutorial.pdf"]),
    ("scince", ["scinceFiles.ebook"]),
    ("math", ["math_Problems.py"]),
])
def test_getfilesWP(riordinato_instance, prefix, expected):
    """Test getfilesWP method"""
    assert riordinato_instance.getfilesWP(prefix) == expected


def test_getfiles(tmp_path, riordinato_instance):
    """test getfiles method"""
    assert get_tmp_files(tmp_path) == riordinato_instance.files


def test_path_is_absolute(riordinato_instance):
    """tests if the path attribute is always an absolute path"""
    assert riordinato_instance.path.is_absolute()
    # change the path
    riordinato_instance.path = "./python"
    assert riordinato_instance.path.is_absolute()


def test_moveSpecificFiles(tmp_path, riordinato_instance):
    """test moveSpecificFiles method"""
    riordinato_instance._moveSpecificFiles('python', tmp_path.joinpath('python'))
    expected = ['pythonCourse.txt', 'Python_tutorial.pdf']
    
    assert get_tmp_files(tmp_path.joinpath('python')) == expected
    

@pytest.mark.parametrize("specificp, ignorep, expected", [
    # Move all files that have a prefix
    (None, None,
     {
         "python": ['pythonCourse.txt', 'Python_tutorial.pdf'],
         "scince":['scinceFiles.ebook'],
         "math":['math_Problems.py'],
         ".":['SpamFiles.lol', 'index.html'],
     }),
    # Move files that only have python prefix
    ("python", None,
     {
         "python": ['pythonCourse.txt', 'Python_tutorial.pdf'],
         ".":['SpamFiles.lol', 'index.html',
              'scinceFiles.ebook', 'math_Problems.py']
     }),
    # Move files that only have python and math prefix
    (["python", "math"], None,
     {
         "python": ['pythonCourse.txt', 'Python_tutorial.pdf'],
         "math":['math_Problems.py'],
         ".":['SpamFiles.lol', 'index.html', 'scinceFiles.ebook', ]
    }),
    # Move all files except those with the scince prefix
    (None, "scince",
     {
         "python": ['pythonCourse.txt', 'Python_tutorial.pdf'],
         "math":['math_Problems.py'],
         ".":['SpamFiles.lol', 'index.html', 'scinceFiles.ebook', ]
     }),
    # move all files except those with math and python prefixes
    (None, ["scince", "math"],
     {
        "python": ['pythonCourse.txt', 'Python_tutorial.pdf'],
        ".":['SpamFiles.lol', 'index.html',
             'scinceFiles.ebook', 'math_Problems.py']
    }),
    # This should not move any files
    (["python", "scince", "math"], ["python", "scince", "math"],
     {
         "python": [],
         "scince":[],
         "math":[],
    })
])
def test_movefiles(tmp_path, riordinato_instance, specificp, ignorep, expected):
    """ test movefiles method"""
    riordinato_instance.movefiles(specific=specificp, ignore=ignorep)

    for dir in list(expected):
        files = get_tmp_files(tmp_path.joinpath(dir))
        assert files == expected[dir]

# TODO: create a test for addprefix method
