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


@pytest.fixture
def instance(tmp_path):
    files = ["pythonTutorial.py", "mathExercise.txt", "pythonCourse.txt",
             "pythonPro.docx", "Python_is_cool.py", "mathProblems.txt",
             "ScinceU.docx", "ThisIsSpam.xd", "mathForPython.pdf",
             "MoreSpam.toml", "scinceForComputing.epup", "asdkfñlk.idk", ]

    dirs = ["python", "scince", "math"]

    create(tmp_path, files, dirs)

    prefixes = [('python', tmp_path / 'python'),
                ('scince', tmp_path / 'scince'),
                ('math', tmp_path / 'math')]
    instance = Riordinato(prefixes, tmp_path)
    return instance


@pytest.fixture
def empty_instance(tmp_path):
    """An instance of the class without files"""
    create(tmp_path, [], [])
    empty = Riordinato([], tmp_path)
    return empty


# test data for parametrize
test_data = pytest.mark.parametrize(
    "prefix, expected",
    [
        ("python",
         ['Python_is_cool.py', 'pythonTutorial.py',
          'pythonCourse.txt', 'pythonPro.docx', ]),

        ("math",
         ['mathForPython.pdf', 'mathProblems.txt',
          'mathExercise.txt', ]),

        ("scince",
         ['scinceForComputing.epup', 'ScinceU.docx']),
    ]
)


@test_data
def test_getFilesWP(instance, prefix, expected):
    assert instance.getFilesWP(prefix) == expected


def test_empty_getFilesWP(empty_instance):
    assert empty_instance.getFilesWP('prefix') == []


def test_getFiles(tmp_path, instance):
    expected_files = get_tmp_files(tmp_path)

    assert instance.files == expected_files


def test_empty_getFiles(empty_instance):
    assert empty_instance.getFiles() == []


@test_data
def test_all_moveFiles(tmp_path, instance, prefix, expected):
    instance.moveFiles()
    files = get_tmp_files(tmp_path / prefix)

    assert files == expected


# TODO: make this test general purpose for the moveFiles method
@pytest.mark.parametrize("specific_prefix, expected_files", [
    (["python", "math"],
     ['scinceForComputing.epup', 'ScinceU.docx', 'asdkfñlk.idk',
      'ThisIsSpam.xd', 'MoreSpam.toml']),
    ("scince",
     ['Python_is_cool.py', 'mathForPython.pdf', 'asdkfñlk.idk',
      'mathProblems.txt', 'ThisIsSpam.xd', 'pythonTutorial.py',
      'pythonCourse.txt', 'mathExercise.txt', 'MoreSpam.toml',
      'pythonPro.docx']),
    (["python", "math", "scince"],
     ['asdkfñlk.idk', 'ThisIsSpam.xd', 'MoreSpam.toml']),
    (None,
     ['asdkfñlk.idk', 'ThisIsSpam.xd', 'MoreSpam.toml'],)
])
def test_specific_moveFiles(tmp_path, instance, specific_prefix, expected_files):
    instance.moveFiles(specific=specific_prefix)
    # files = get_tmp_files(tmp_path)

    assert instance.files == expected_files


@pytest.mark.parametrize("ignore", [
    "python",
    "math",
    "scince",
])
# TODO: rewrite this test
def test_ingore_moveFiles(instance, tmp_path, ignore):
    instance.moveFiles(ignore=ignore)
    files = get_tmp_files(tmp_path / ignore)

    assert files == []


@test_data
def test_moveSpecificFiles(tmp_path, instance, prefix, expected):
    instance.moveSpecificFiles(prefix, tmp_path / prefix)
    files = get_tmp_files(tmp_path / prefix)

    assert files == expected
