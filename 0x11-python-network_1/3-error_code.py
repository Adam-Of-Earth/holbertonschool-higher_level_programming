#!/usr/bin/python3
"""displays body of a URL"""

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = argv[1]
    request = request.Request(url)
    try:
        with request.urlopen(request) as response:
            print(response.read().decode('urf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
