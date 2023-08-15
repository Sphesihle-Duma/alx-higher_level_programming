#!/usr/bin/python3
"""Base module for a base class
"""
import json


class Base:
    """Base class for all classes in the
    modules
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor that will be used to
        create an object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json representation
        of list_objs to file
        Args
            list_objs: list of objects
        """
        json_string = cls.to_json_string(list_objs)
        with open(Base.json, "W", encoding="UTF-8") as f:
            f.write(json_string)
