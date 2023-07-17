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

     def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
