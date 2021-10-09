#!/usr/bin/python3
"""
Write a Python script that takes your Github credentials (username and
password) and uses the Github API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    try:
        user = requests.get(url, auth=(argv[1], argv[2])).json()

        if "id" in user:
            print(user["id"])
        else:
            print("None")
    except:
        print("None")
