# Riordinato

Riordinato is a python library for organizing files with prefixes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install riordinato.

```bash
pip install riordinato 
```

## Usage

Riordinato is used to organize files by prefixes. For example, we want to move the files that have python in their name to the python folder and similar with the files that have work.

```
/home/user/documents
├── pythonWork.py
├── python_examples.txt
├── family.jpg
├── dog.png
├── index.html
├── work_list.txt
├── any_work.docx
├── python_exercise.pdf
├── work_for_later.docx
│
├── python/
└── work/
```

First import riordinato

```py
from riordinato.files import Organize
```

The prefixes are within a list where the first value is the name and the second the destination.

```py
            #  NAME            DESTINATION
prefixes = [('python', '/home/user/documents/python')
            ('work', '/home/user/documets/work')]
# You can also use windows directory syntax

```

We define a directory where we have the files we want to move.

```py
path = '/home/user/documents'
```

We create the instance.

```py
organize = Organize(prefixes, path)
```

If you want to see the files that are in the path you can print the files attribute.

```py
>>> print(organize.files)

['pythonWork.py', 'python_examples.txt', 'family.jpg', 'dog.png', 'index.html', 
'work_list.txt', 'any_work.docx', 'work_for_later.docx', 'python_exercise.pdf']
```

To organize our files we use the moveFiles method

```py
organize.moveFiles()
```

And our directory would look like this.

```
/home/user/documents
├── family.jpg
├── dog.png
├── index.html
├── any_work.docx          
│
├── python/
│   ├── python_exercise.pdf
│   ├── pythonWork.py
│   └── python_examples.txt
└── work/
    ├── work_for_later.docx
    └── work_list.txt
```

If we want to move files with a specific prefix, use the "specific" parameter of the method.

```py
organize.moveFiles(specific='python')
```

```
/home/user/documents
├── family.jpg
├── dog.png
├── index.html
├── work_list.txt
├── work_for_later.docx
├── any_work.docx
│
├── python/
│   ├── python_exercise.pdf
│   ├── pythonWork.py
│   └── python_examples.txt
└── work/
    
```

## Contributing
A contributing.md will be added soon.

## License
[MIT](https://choosealicense.com/licenses/mit/)
