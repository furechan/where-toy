""" Utility to locate modules in the python path """

import argparse
import importlib.util

from pathlib import Path


# TODO use pkgutil to iter modules ?


def find_module(module, recurse=False):
    """ locates and displays module location/contents """

    spec = importlib.util.find_spec(module)

    if not spec:
        print("%s not found!" % module)
        return

    if spec.origin:
        file = Path(spec.origin)
        print("origin", file)

    if spec.submodule_search_locations:
        for p in spec.submodule_search_locations:
            print("location", p)

    if recurse and spec.submodule_search_locations:
        locations = spec.submodule_search_locations
        files = [f for p in locations for f in Path(p).glob("*.py")]
        total_size = 0
        for file in files:
            size = file.stat().st_size
            total_size += size
            print(file)

        print("Total size", total_size)


def main():
    parser = argparse.ArgumentParser(description=__doc__, prog='python -mwhere')
    parser.add_argument('-r', '--recurse', action='store_true', help="iterates over package contents")
    parser.add_argument('module', help="module or package name")

    options = parser.parse_args()

    module = options.module
    recurse = options.recurse

    find_module(module, recurse=recurse)


if __name__ == "__main__":
    main()
