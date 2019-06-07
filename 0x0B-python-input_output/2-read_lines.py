#!/usr/bin/python3
"""module to read a number of lines"""


def read_lines(filename="", nb_lines=0):
    """prints lines from a file"""
    with open(filename, encoding="UTF-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
            return
        for i in range(nb_lines):
            print(myFile.readline(), end="")
