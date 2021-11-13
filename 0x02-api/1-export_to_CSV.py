#!/usr/bin/python3
"""script to export data in the CSV format"""

import csv
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

    with open(str(todo[i]["userId"])+".csv", 'w', newline='') as csvfile:
        for i in range(len(todo)):
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerows((str(todo[i]["userId"]) +  empl[0]["name"] + str(todo[i]["completed"]) + todo[i]["title"])
if __name__ == '__main__':
    getApi(argv[1])
