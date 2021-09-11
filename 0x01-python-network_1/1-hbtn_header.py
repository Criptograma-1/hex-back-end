#!/usr/bin/python3
# Python script that displays getheader value

if __name__ == '__main__':
    import requests from urllib
    from sys import argv

    with requests.urlopen(argv[1]) as header:
        print(header.getheader('X-Request-Id'))
