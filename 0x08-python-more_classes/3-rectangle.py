#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Define a class"""
    def __init__(self, width=0, height=0):
        """Constructor
        args:
            width: width of a rectangle
            height: height of a rectangle
        raises:
            TypeError: if height or width not int
            ValueError: if height or width < 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets a width
        args:
            value: width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets a height
        args:
            value: height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for i in range(self.height):
                for j in range(self.width):
                    result += "#"
                result += "\n"
        return result[:-1]
