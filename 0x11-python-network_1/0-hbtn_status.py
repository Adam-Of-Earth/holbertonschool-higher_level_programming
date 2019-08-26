#!/usr/bin/python3
"""script to download a page"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_type = type(html)
        print("body response:")
        print("\t- type: {}".format(html_type))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
