#!/usr/bin/python3
"""script that displays the X-Request-Id"""

import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
