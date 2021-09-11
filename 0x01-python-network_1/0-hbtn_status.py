#!/usr/bin/python3
"""
Contains a Python script that fetches https://intranet.hbtn.io/status.
"""
import requests from urllib


def run():
    """
    Fetches https://intranet.hbtn.io/status.
    """
    url = 'https://intranet.hbtn.io/status'
    with requests.urlopen(url) as res:
        r = res.read()
        print('Body response:')
        print('\t- type:', type(r))
        print('\t- content:', r)
        print('\t- utf8 content:', r.decode('utf-8'))


if __name__ == "__main__":
    """
    Fetches https://intranet.hbtn.io/status.
    """
    run()
