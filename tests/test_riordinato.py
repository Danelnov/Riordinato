from riordinato.files import Organize
import pytest


@pytest.fixture
def files():
    newFiles = ["pythonTutorial.py", "mathExercise.txt", "pythonCourse.txt",
                "pythonPro.docx", "Python_is_cool.py", "mathProblems.txt",
                "ScinceU.docx", "ThisIsSpam.xd", "mathForPython.pdf",
                "MoreSpam.toml", "scinceForComputing.epup", "asdkfñlk.idk"]

    instance = Organize("", ".")
    instance.files = newFiles
    return instance


@pytest.mark.parametrize(
    "prefix, expected",
    [
        ("python",
         ['pythonTutorial.py', 'pythonCourse.txt',
          'pythonPro.docx', 'Python_is_cool.py']),

        ("math",
         ['mathExercise.txt', 'mathProblems.txt',
          'mathForPython.pdf']),

        ("scince",
         ['ScinceU.docx', 'scinceForComputing.epup'])
    ]
)
def test_getFilesWP(files, prefix, expected):
    assert files.getFilesWP(prefix) == expected
