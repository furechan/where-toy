# Utility to locate python modules from the command line 


## Warning
This project installs a module called ```where```
which might collide with modules of the same name from other pypi distributions like [where](https://pypi.org/project/where/).
Make sure to install the one you are looking for.



## Usage

Used from the command line by invoking ```python -mwhere <module>```
The module is a thin layer around ```importlib``` to display the location of a module or package.
It works also for native namespace packages in which case it will list the containing folders.


```console
python -mwhere [-h] [-r] module
```

## Command line options
The recurse ```-r``` option will also list the contained submodules.

```console
positional arguments:
  module         module or package name

optional arguments:
  -h, --help     show this help message and exit
  -r, --recurse  iterates over package contents
```

## Some Examples
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

TODO Add tests
