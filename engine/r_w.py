#!/usr/bin/python3
'''
    Read the actors.json file, read its content, call an algorithm function
    and write result to result.json file
'''
import json
from search import *


def read_input():
    ''' Read and write to JSON file'''
    with open('../actors.json', 'r') as f:
        data = json.load(f)
        actor1 = data['actor1']
        actor2 = data['actor2']

    result = call_api('actor1', 'actor2')

    with open('../result.json', 'w') as f:
        json.dump(result, f)


if __name__ == "__main__":
    read_input()
