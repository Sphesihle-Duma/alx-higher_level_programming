#!/usr/bin/python3
"""Base module for a base class
"""


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
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
