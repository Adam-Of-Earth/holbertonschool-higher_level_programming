#!/usr/bin/python3
"""fetches status of URL"""
import requests


if __name__ == "__main__":
    reques = requests.get('https://intranet.hbtn.io/status')
    text = reques.text
    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
