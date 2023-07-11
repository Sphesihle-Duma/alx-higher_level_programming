#!/usr/bin/python3
"""Appending module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a txt file
    Args:
        filename: name of a file
        text: text to be appended
    """
    with open(filename, "a+", encoding="utf") as f:
        f.write(text)
