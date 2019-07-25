#!/usr/bin/python3
"""Function to get dict of JSON"""


def class_to_json(obj):
    """Return dict containing JSON-serializable"""

    allowed = (list, dict, str, int, bool)
    return {k: v for k, v in obj.__dict__.items() if isinstance(v, allowed)}
