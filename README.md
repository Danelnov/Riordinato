<div align="center">
    <h1>Riordinato</h1>
    <h4>Riordinato is a python library for organizing files with prefixes.</h4>
</div>

<div align="center" width="60%" height="auto">
    <img src="./resources/riordinato_cli.gif">
</div>

## Installation

Use the package manager [pip](https://pypi.org/project/riordinato/) to install riordinato.

```console
$ pip install riordinato 
```

## Use the cli

Riordinato includes a cli so you can organize all your files from the terminal.

First you must go to the directory where you want riordinato to organize your files, then you must start the database with:

```console
$ riordinato init
```

Now you have to add a prefix and a directory path.

```console
$ riordinato add <prefix> <path>
```

Now to organize your files put:

```console
$ riordinato organize
```

If you want to know more about the cli read the documentation [here](./cli_docs.md).

## Usage

Riordinato is used to organize files by prefixes. For example, we want to move files that have the prefixes python and work.

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
from riordinato import Riordinato
```

Define a directory where we have the files we want to move.

```py
path = '/home/user/documents'
```
> **_NOTE:_** You can also put a windows path.

Create the instance.

```py
organize = Riordinato(path)
```

If you want to see the files that are in the path you can print the files attribute.

```py
>>> print(organize.files)

['pythonWork.py', 'python_examples.txt', 'family.jpg', 'dog.png', 'index.html', 
'work_list.txt', 'any_work.docx', 'work_for_later.docx', 'python_exercise.pdf']
```

Now you have to create a prefix. to do it is the same when you create a new item for a dictionary, the key is the prefix and the value is the destination

```py
organize.prefixes['python'] = './python'
organize.prefixes['work'] = './work' 
```
> **_NOTE:_** Riordinato by default transforms all paths into an absolute path. This allows your program to run from any path.

To organize our files we use the movefiles method

```py
organize.movefiles()
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
organize.movefiles(specific='python')
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

You can also ignore files that contain a certain prefix. In this case we will ignore the files that contain the python prefix.

```py
organize.movefile(ignore='python')
```

```
/home/user/documents
    ├── pythonWork.py
    ├── python_examples.txt
    ├── family.jpg
    ├── dog.png
    ├── index.html
    ├── any_work.docx
    ├── python_exercise.pdf
    │
    ├── python/
    └── work/
        ├── work_for_later.docx
        └── work_list.txt
```

> **_NOTE:_** the specific and ignore parameters are also compatible with lists.

## Contributing
A contributing.md will be added soon.

## License
[MIT](https://choosealicense.com/licenses/mit/)
