#!/usr/bin/python3
"""sends POST request to url"""

import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
