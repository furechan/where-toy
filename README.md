# Utility to locate python modules from the command line 

This module is pre-alpha level.

Meant to be used from the command line by invoking ```python -mwhere module```
A thin layer around importlib to display the location of a module or package.
It works also for native namespace packages that can span across multiple foldrers. 

# Usage

```console
python -mwhere.py [-h] [-r] module
```

# Options

```console
positional arguments:
  module         module or package name

optional arguments:
  -h, --help     show this help message and exit
  -r, --recurse  iterates over package contents
```

# Locate a module or package
```console
$> python -mwhere sysconfig 
origin C:\Users\...\envs\py38\lib\sysconfig.py

$> python -mwhere pandas      
origin C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
location C:\Users\...\envs\py38\lib\site-packages\pandas
```

# List package contents with recurse option
```console
$> python -mwhere pandas -r 
origin C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
location C:\Users\...\envs\py38\lib\site-packages\pandas
C:\Users\...\envs\py38\lib\site-packages\pandas\conftest.py
C:\Users\...\envs\py38\lib\site-packages\pandas\testing.py
C:\Users\...\envs\py38\lib\site-packages\pandas\_typing.py
C:\Users\...\envs\py38\lib\site-packages\pandas\_version.py
C:\Users\...\envs\py38\lib\site-packages\pandas\__init__.py
Total size 66482
```

