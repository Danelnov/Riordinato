# `riordinato`

Organize your files by prefixes.

**Usage**:

```console
$ riordinato [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a new prefix to the json file.
* `init`: Create prefixes.json file in current...
* `organize`: Organize files that have prefixes.
* `remove`: Remove prefixes.

## `riordinato add`

Add a new prefix to the json file.

**Usage**:

```console
$ riordinato add [OPTIONS] PREFIX DESTINATION
```

**Arguments**:

* `PREFIX`: The prefix that the file names should have.  [required]
* `DESTINATION`: The directory where the files with the prefix will be moved.  [required]

**Options**:

* `--ignore / --no-ignore`: Ignore the prefixes.json file inside the directory.
* `--help`: Show this message and exit.

## `riordinato init`

Create prefixes.json file in current directory.

**Usage**:

```console
$ riordinato init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `riordinato organize`

Organize files that have prefixes.

**Usage**:

```console
$ riordinato organize [OPTIONS]
```

**Options**:

* `--ignore / --no-ignore`: Ignore the prefixes.json file inside the directory.
* `--specific TEXT`: Only move files containing these prefixes.
* `--exclude TEXT`: Ignore all files with these prefixes.
* `--help`: Show this message and exit.

## `riordinato remove`

Remove prefixes.

**Usage**:

```console
$ riordinato remove [OPTIONS] PREFIXES...
```

**Arguments**:

* `PREFIXES...`: The prefixes to be removed from the database.  [required]

**Options**:

* `--ignore / --no-ignore`: Ignore the prefixes.json file inside the directory.
* `--help`: Show this message and exit.
