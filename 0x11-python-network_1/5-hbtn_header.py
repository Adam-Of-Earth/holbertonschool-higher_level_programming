#!/usr/bin/python3
"""script that sends a request to a URL and displays X-Request-Id"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
