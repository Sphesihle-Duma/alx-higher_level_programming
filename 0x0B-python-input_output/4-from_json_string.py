#!/usr/bin/python3
"""json to object
"""
import json


def from_json_string(my_str):
    """Convert string to json
    Args:
        my_str: string to be converted
    Return
        object represented by JSON string
    """
    return json.loads(my_str)
