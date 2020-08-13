# Riordinato

Riordinato is a python library for organizing files with prefixes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install riordinato.

```bash
pip install riordinato 
```

## Usage

```python
from riordinato.files import Organize

# Example
# Prefix: 'python'
# destination folder: '/home/user/documents/pythonfiles'
prefixes = [('<prefix>', '<destination folder>'),
            ('<prefix>', '<destination folder>')]

# this variable represents the location of the folder that riordinato is going to organize
dir = '/home/user/any folder'

organize = Organize(prefixes, dir)

# Organize all files in the folder
organize.organize_all()

# organizes only files containing the specified prefix
organize.organize_specific_files('<prefix>')


```

## Contributing
Any pull request is welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
