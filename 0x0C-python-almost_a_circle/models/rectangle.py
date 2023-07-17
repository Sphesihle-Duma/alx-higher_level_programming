#!/usr/bin/python3
"""Rectangle class that
inherits base class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be => 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be => 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

    @property
    def width(self):
        """Return the width of a rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """setter method for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Return the height of a rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """setter method for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Returns the x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """setter method for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be => 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be => 0")
        else:
            self.__y = y
