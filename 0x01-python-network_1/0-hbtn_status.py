#!/usr/bin/python3
"""urllib package"""
import requests from urllib


if __name__ == "__main__":
    """script that fetches https://intranet.hbtn.io/status"""
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        """Print a response and response type"""
        response = response.read()
        print("Body response:")
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
