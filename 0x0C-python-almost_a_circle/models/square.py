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
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value
