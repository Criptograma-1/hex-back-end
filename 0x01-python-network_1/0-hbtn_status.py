#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import requests from urllib 


def urlRequest():
    """ Function that makes a request to a url """
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        """ Function that makes a request to a url """
        response = response.read()
    """ Function that makes a request to a url """
    print("Body response:")
    print("- type: {}".format(type(response)))
    print("- content: {}".format(response))

if __name__ == "__main__":
    """ Function that makes a request to a url """
    urlRequest()
