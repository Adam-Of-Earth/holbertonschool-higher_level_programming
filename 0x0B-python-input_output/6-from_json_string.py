#!/usr/bin/python3
"""function to deserialize JSON"""


import json


def from_json_string(my_str):
    """deserialize JSON file"""

    return json.loads(my_str)
