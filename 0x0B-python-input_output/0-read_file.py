#!/usr/bin/python3
"""Reading file module
"""


def read_file(filename=""):
    """Read a file function
    Args:
        filename: filename
    Prints:
        print data read
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
