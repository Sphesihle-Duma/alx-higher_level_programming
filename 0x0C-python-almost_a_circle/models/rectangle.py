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
        self.__width = width

    @property
    def height(self):
        """Return the height of a rectangle"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """setter method for height"""
        self.__height = height

    @property
    def x(self):
        """Returns the x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """setter method for x"""
        self.__x = x

    @property
    def y(self, y):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self):
        """setter method for y"""
        self.__y = y
