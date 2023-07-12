#!/usr/bin/python3
"""class to json module
"""


def class_to_json(obj):
    """returns the dictionary description with simple
    data structure
    Args:
        obj: object
    return:
        dictionary representation
    """
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        return result
