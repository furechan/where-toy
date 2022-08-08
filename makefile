# for use in windows only ...
# requires setuptools build twine
# makefile should be tab indented !

version = 0.0.1
name = where-toy
lcname = where_toy

dist: FORCE
	call python -m build .

dump: FORCE
	tar -tvf dist/$(name)-$(version).tar.gz
	unzip -l dist/$(lcname)-*-py3-none-any.whl

install: FORCE
	python setup.py develop

remove: FORCE
	python setup.py develop -u

upload: FORCE
	call twine upload --repository testpypi dist/*

FORCE:

