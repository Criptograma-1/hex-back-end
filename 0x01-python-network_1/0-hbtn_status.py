#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    """Import requests"""
    import requests from urllib

    """fetches https://intranet.hbtn.io/status"""
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        """Print response"""
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
