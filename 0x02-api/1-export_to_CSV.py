#!/usr/bin/python3
"""script to export data in the CSV format"""


import requests as res
from sys import argv


def getApi(u):
    """A function that returns to do list"""
    user = int(u)
    done = 0
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user}).json()
    empl = res.get('https://jsonplaceholder.typicode.com/users',
                   params={'id': user}).json()
    
    for i in range(len(todo)):
        print(todo[i]["userId"],empl[i]["name"],todo[i]["completed"],todo[i]["title"])


if __name__ == '__main__':
    getApi(argv[1])
