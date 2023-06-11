#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    last_element_idx = -1
    while length > 0:
        if length <= len(my_list):
            print("{:d}".format(my_list[last_element_idx]))
        length = length - 1
        last_element_idx = last_element_idx - 1
