#!/usr/bin/python3
'''implementation of the engine to get information about actors'''
import requests

def call_api(a1, a2):
    '''calls the movies api to get the actors and movies'''
    name = a1.replace(" ", "+")
    url = "http://www.theimdbapi.org/api/find/person?name={}".format(name)
    results = requests.get(url)
    contents = results.json()[0]
    try:
        films = contents["filmography"]["actor"]
    except KeyError:
        films = contents["filmography"]["actress"]

    list_films = {}
    for movie in films:
        if movie["type"] == "Film":
            list_films[movie["title"]] = movie["imdb_id"]

    name2 = a2.replace(" ", "+")
    url = "http://www.theimdbapi.org/api/find/person?name={}".format(name2)
    results = requests.get(url)
    contents = results.json()[0]
    try:
        films = contents["filmography"]["actor"]
    except KeyError:
        films = contents["filmography"]["actress"]
    list_films2 = {}
    for movie in films:
        if movie["type"] == "Film":
            list_films2[movie["title"]] = movie["imdb_id"]

    if set(list_films2.keys()) & set(list_films.keys()):
        results = list(set(list_films2.keys()).intersection(list_films.keys()))
        return [{"name1": name.replace("+", " "),
                 "movie": results,
                 "name2": name2.replace("+", " "),
                 "error": False}]
    else:
        print ("nothing")

if __name__ == "__main__":
    call_api("brad pitt", "angelina jolie")
    call_api("Meryl Streep","Daniel Day Lewis")