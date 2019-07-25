#!/usr/bin/python3
"""load objects from JSON files"""


import json


def load_from_json_file(filename):
    """Return object from JSON file"""

    with open(filename, 'rt', encoding='UTF-8') as file:
        return json.load(file)
