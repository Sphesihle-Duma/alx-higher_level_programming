#!/bin/usr/python3
"""look up module"""


def lookup(obj):
    """Prints all members of obj
    args:
        obj: object
    Return: list
    """
    return dir(obj)
