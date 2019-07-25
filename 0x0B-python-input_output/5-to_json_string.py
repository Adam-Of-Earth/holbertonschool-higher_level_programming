#!/usr/bin/python3
"""function to serialize JSON"""


import json


def to_json_string(my_obj):
    """Return serilaztion of JSON"""

    return json.dumps(my_obj)
