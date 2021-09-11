#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import requests from urllib


if __name__ == "__main__":
    """"Function that makes a request to a url"""
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
        print("Body response:")
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
