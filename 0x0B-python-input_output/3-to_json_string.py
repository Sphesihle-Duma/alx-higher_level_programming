#!/usr/bin/python3
"""JSON representation module
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj
    Args:
        my_obj: an object to be conveted
    Return:
        JSON representation
    """
    return json.dumps(my_obj)
