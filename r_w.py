#!/usr/bin/python3
''' 
    Read the actors.json file, read its content, call an algorithm function
    and write result to result.json file
'''
import json


def read_input():
    ''' Read and write to JSON file'''
    with open('../actors.json', 'r') as f:
        data = json.loads(f)
        actor1 = data['actor1']
        actor2 = data['actor2']

    result = find_relation(actor1, actor2)

    with open('../result.json', 'w') as f:
        json.dump(result, f)
