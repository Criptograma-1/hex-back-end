#!/usr/bin/python3
"""urllib package"""


import requests from urllib


if __name__ == "__main__":
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
        print("Body response:")
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
