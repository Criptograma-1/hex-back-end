#!/usr/bin/python3
"""
script that use REST API for returns information
about employee TODO list progress
"""


import json
import requests as res
from sys import argv


def getApi(u):
    """A function that returns to do list"""
    user = int(u)
    done = 0
    todo = res.get('https://jsonplaceholder.typicode.com/todos',
                   params={'userId': user})
    em = res.get('https://jsonplaceholder.typicode.com/users',
                 params={'id': user})
    empl = json.loads(em.text)
    td = json.loads(todo.text)

    for i in range(len(td)):
        if td[i]['completed'] is True:
            done = done+1
    undone = len(td)
    name = empl[0]['name']
    print("Employee {} is done with tasks({}/{}):".format(name, done, undone))

    for i in range(len(td)):
        if td[i]['completed'] is True:
            print("\t {}".format(td[i]['title']))


if __name__ == '__main__':
    getApi(argv[1])
