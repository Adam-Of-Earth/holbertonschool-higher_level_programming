#!/usr/bin/python3
"""displays body of a URL"""

import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('urf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
