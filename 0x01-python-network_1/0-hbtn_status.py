#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request


def urlRequest():
    """ Function that makes a request to a url """
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
    print("Body response:")
    print("- type: {}".format(type(response)))
    print("- content: {}".format(response))

if __name__ == "__main__":
    urlRequest()
