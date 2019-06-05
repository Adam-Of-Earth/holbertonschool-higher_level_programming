#!/usr/bin/python3
"""Checks to see if object is subclass"""


def inherits_from(obj, a_class):
    """checks if is subclass"""
    return isinstance(obj, a_class) and type(obj) is not a_class
