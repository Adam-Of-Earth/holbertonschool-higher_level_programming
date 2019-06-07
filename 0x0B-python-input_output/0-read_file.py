#!/usr/bin/python3
"""module to read text file"""


def read_file(filename=""):
    """fuction to read file"""

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
