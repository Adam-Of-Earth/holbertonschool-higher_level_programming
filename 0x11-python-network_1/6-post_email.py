#!/usr/bin/python3
"""script that takes URL and email displaying body"""
import requests
import sys

if __name__ == "__main__":
    reques = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(reques.text)
