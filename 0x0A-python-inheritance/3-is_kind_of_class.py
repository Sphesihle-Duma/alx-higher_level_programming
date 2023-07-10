#!/usr/bin/python3
"""checks type of the including
super class
"""


def is_kind_of_class(obj, a_class):
    """checks the kind of a class
    Args:
        obj: object
        a_class: class
    return:
        True is the obj is a member of a
        class or super class otherwise
        False
    """
    return isinstance(obj, a_class)
