# Utility to locate python modules from the command line 

Python utility to locate packages or resources in the python path.
The module is a thin layer around `importlib` to display
the location and contents of an installed module or package.
The script exits with an error code if the module is not found.
This is similar to `python -minspect <name> -d` but adds the option
to display the package contents as a tree.

## Usage

```console
Usage: python -m where [OPTIONS] MODULE

  Locate python module or resources in the python path

  MODULE is the name of a module or package as a fully qualified
  python name

Options:
  -r, --recurse  Recurse into directory contents
  --help         Show this message and exit.
```


## Examples

```console
> python -mwhere sysconfig 
/Users/.../envs/py38/lib/sysconfig.py

> python -mwhere pandas      
/Users/.../envs/py38/lib/site-packages/pandas/__init__.py

> python -mwhere where -r
/Users/../Projects/where-toy/src/where
├── __init__.py
├── __main__.py
└── utils.py
```

## Installation

> **Warning**
This project installs a module called ```where```
which name is also used by other projects like
[where](https://pypi.org/project/where/).

You can install the latest version of this module with `pip

```console
pip install git+ssh://git@github.com/furechan/where-toy.git
```

## Related Projects & Resources
- [pyloc](https://github.com/nicolasdespres/pyloc) Locate python object definition in your file-system
- [inspect](https://docs.python.org/3/library/inspect.html#command-line-interface) inspect module command line interface
