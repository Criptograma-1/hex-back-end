#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import requests from urllib

"""Print a response and response type"""
if __name__ == "__main__":
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
        print("Body response:")
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
