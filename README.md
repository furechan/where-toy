# Utility to locate python modules from the command line 

Python utility to locate any module in the python path.
The module is a thin layer around ```importlib``` to display
the location and containing folders of a module or package.
The script exits with an error code if the module is not found.

> **Warning**
This project installs a module called ```where```
which name is also used by other projects like
[where](https://pypi.org/project/where/).
Make sure to install the one you are looking for!

## Usage

Used from the command line by invoking ```python -mwhere module```

```console
python -mwhere [-h] [-t] module

positional arguments:
  module         module or package name

optional arguments:
  -h, --help     show this help message and exit
  -t, --tree     print tree of files
```

Please note the `-t` option to print the package contents as a tree.


## Examples

```console
$> python -mwhere sysconfig 
/Users/bob/envs/py38/lib/sysconfig.py

$> python -mwhere pandas      
/Users/bob/envs/py38/lib/site-packages/pandas/__init__.py

$> python -mwhere where -t 
/Users/bob/Projects/Python/where-toy/src/where
├── __init__.py
├── __main__.py
└── utils.py
```

## Installation

You can install the latest version of this module with pip

```console
pip3 install git+https://github.com/furechan/where-toy.git
```

