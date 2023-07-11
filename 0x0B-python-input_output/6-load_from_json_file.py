#!/usr/bin/python3
"""load from json module
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
        filename: name of a file
    Return:
        Nothing
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
