#!/usr/bin/python3
""" checking type function
"""


def is_same_class(obj, a_class):
    """ checks if the object is
    of the type of the specified class
    Args:
        obj: object to check
        a_class: class
    Return:
        True if obj is a member of the
        class otherwise false
    """
    return type(obj) is a_class
