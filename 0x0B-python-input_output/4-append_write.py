#!/usr/bin/python3
"""module to append to a file"""


def append_write(filename="", text=""):
    """function to append text file"""

    with open(filename, "at", encoding="UTF-8") as myFile:
        myFile.write(text)
    return len(text)
