#!/usr/bin/python3
"""Square module inherit
base class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation
        """
        first = "[Square]"
        second = " ({})".format(self.id)
        third = " {}/{}".format(self.x, self.y)
        fourth = " - {}".format(self.width)
        return first + second + third + fourth

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the attribute
        """
        if args:
            num_args = len(args)
            attr_names = ["id", 'size', "x", "y"]
            for i in range(min(num_args, len(attr_names))):
                setattr(self, attr_names[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

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
