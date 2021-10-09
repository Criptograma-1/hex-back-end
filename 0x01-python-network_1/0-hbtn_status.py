#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

""" Function that makes a request to a url."""
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
