#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        response = response.read()
        print("Body response:")
        print(" - type: {}".format(type(response)))
        print(" - content: {}".format(response))
