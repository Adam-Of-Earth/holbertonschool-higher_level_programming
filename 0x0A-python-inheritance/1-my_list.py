#!/usr/bin/python3
"""method to inherit from a list"""


class MyList(list):
    """class to inherit list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
