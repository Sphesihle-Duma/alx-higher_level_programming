#!/usr/bin/python3
"""Student Module
"""


class Student:
    """student class
    """
    first_name
    last_name
    age

    def __init__(self, first_name, last_name, age):
        """constructor
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation"""
        return self.__dict__.copy()
