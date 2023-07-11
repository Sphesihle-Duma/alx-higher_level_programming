#!/usr/bin/python3
"""save_to_json module
"""
import json


def save_to_json_file(my_obj, filename):
    """writes my_obj to filename
    Args:
        my_obj: object to be written on the file
        filename: to write on
    """
    with open(filename, "w", encoding="utf-8") as f:
        obj = json.dumps(my_obj)
        f.write(obj)
