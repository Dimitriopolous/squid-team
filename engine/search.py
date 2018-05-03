#!/usr/bin/python3
'''implementation of the engine'''
import requests

def call_api(a1, a2):
    name = a1.split(" ")
    url = "http://www.theimdbapi.org/api/find/person?name={}+{}".format(name[0],
                                                                        name[1])
    results = requests.get(url)
    print(results.json())


if __name__ == "__main__":
    call_api("jim carrey", "a2")