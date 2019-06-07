#!/usr/bin/python3
"""module to find number of lines"""


def number_of_lines(filename=""):
    """returns number of lines"""
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
        return i
