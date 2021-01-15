from riordinato import Riordinato
import pytest


def create(tmp_path, files, dirs):
    """Create files and directories in a temporal path"""
    # Create files
    for file in files:
        new_file = tmp_path / file
        new_file.touch()

    # Create directories
    for dir in dirs:
        new_dir = tmp_path / dir
        new_dir.mkdir()
        

@pytest.fixture
def instance(tmp_path):
    files = ["pythonCourse.txt", "Python_tutorial.pdf",
             "scinceFiles.ebook", "math_Problems.py",
             "index.html", "SpamFiles.lol",]

    dirs = ["python", "scince", "math"]

    create(tmp_path, files, dirs)

    prefixes = [('python', tmp_path / 'python'),
                ('scince', tmp_path / 'scince'),
                ('math', tmp_path / 'math')]
    instance = Riordinato(tmp_path)
    
    for prefix in prefixes:
        instance.addprefix(prefix[0], prefix[1])
    
    return instance


@pytest.fixture
def empty_instance(tmp_path):
    """An instance of the class without files"""
    create(tmp_path, [], [])
    empty = Riordinato(tmp_path)
    return empty
