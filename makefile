# for use in windows only ...
# requires setuptools build twine
# makefile should be tab indented !

dist: FORCE
	call python -m build --wheel .

dump: FORCE
	unzip -l dist/*-py3-none-any.whl

install: FORCE
	python setup.py develop

remove: FORCE
	python setup.py develop -u

upload: FORCE
	call twine upload dist/*

FORCE:

