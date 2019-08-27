#!/usr/bin/python3
"""sends a request to URL and displays the response"""
import requests
import sys


if __name__ == '__main__':
    reques = requests.get(sys.argv[1])
    if reques.status_code >= 400:
        print("Error code: {}".format(reques.status_code))
    else:
        print(reqst.text)
