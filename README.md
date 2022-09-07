# Utility to locate python modules from the command line 

Python command line utility to locate any module in the python path.
The module is a thin layer around ```importlib``` to display
the location and containing folders of a module or package.
The script exits with an error code if the module is not found.


## Usage

Used from the command line by invoking ```python -mwhere module```

```console
python -mwhere [-h] [-r] module

positional arguments:
  module         module or package name

optional arguments:
  -h, --help     show this help message and exit
  -r, --recurse  iterates over package sub-modules
```

Please note the recurse ```-r``` option to list the package sub-modules.


## Examples

```console
$> python -mwhere sysconfig 
origin C:\Users\...\envs\py38\lib\sysconfig.py

$> python -mwhere pandas      
origin C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
location C:\Users\...\envs\py38\lib\site-packages\pandas

$> python -mwhere pandas -r 
origin C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
location C:\Users\...\envs\py38\lib\site-packages\pandas
C:\Users\...\envs\py38\lib\site-packages\pandas\conftest.py
C:\Users\...\envs\py38\lib\site-packages\pandas\testing.py
C:\Users\...\envs\py38\lib\site-packages\pandas\_typing.py
C:\Users\...\envs\py38\lib\site-packages\pandas\_version.py
C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
...
```

## Installation

> **Note**
This project installs a module called ```where```
which might collide with modules of the same name from other pypi distributions
like [where](https://pypi.org/project/where/).
Make sure to install the one you are looking for!

You can install the latest version of this module with pip

```console
pip3 install git+ssh://git@github.com/furechan/where-toy.git
```

