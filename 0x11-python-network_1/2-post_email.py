#!/usr/bin/python3
"""sends POST request to url"""

from sys import argv
import urllib.parse
import urllib.request


data = urllib.parse.urlencode(email)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
