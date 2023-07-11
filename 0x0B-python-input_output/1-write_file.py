#!/usr/bin/python3
"""Writting to a file module
"""


def write_file(filename="", text=""):
    """Write text to a file
    Args:
        filename: file to write to
        text: text to write on the file
    Return:
        number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        number_of_chars = f.write(text)
        return number_of_chars
