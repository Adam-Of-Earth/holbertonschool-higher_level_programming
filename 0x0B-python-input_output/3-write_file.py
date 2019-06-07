#!/usr/bin/python3
"""module to write to a file"""


def write_file(filename="", text=""):
    """fuction to write to a file"""
    with open(filename, "wt", encoding="UTF-8") as myFile:
        myFile.write(text)
    return len(text)
