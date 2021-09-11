#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    """Import requests"""
    import requests from urllib

    """fetches https://intranet.hbtn.io/status"""
    with requests.urlopen('https://intranet.hbtn.io/status') as response:
        """Python script that fetches https://intranet.hbtn.io/status"""
        html = response.read()
        """Python script that fetches https://intranet.hbtn.io/status"""
        print('Body response:')
        """Python script that fetches https://intranet.hbtn.io/status"""
        print('\t- type: {}'.format(type(html)))
        """Python script that fetches https://intranet.hbtn.io/status"""
        print('\t- content: {}'.format(html))
