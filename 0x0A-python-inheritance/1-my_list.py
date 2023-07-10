#!/usr/bin/python3
""" Mylist module
"""


class MyList(list):
    """class Mylist
    """
    def print_sorted(self):
        """ sorts the list
        args:
            self: object
        Return:
            sorted list
        """
        sorted_l = self.copy()
        sorted_l.sort()
        print(sorted_l)
