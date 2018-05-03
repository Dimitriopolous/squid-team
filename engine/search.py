#!/usr/bin/python3
'''implementation of the engine to get information about actors'''
import requests

def call_api(a1, a2):
    ''' Entry point for two actors to find their degree of relationship'''
    r = []
    mlist1 = get_movies(a1)
    mlist2 = get_movies(a2)

    result = compare(mlist1, mlist2, a1, a2)
    if result is not False:
        print('found level 1')
        return result
    for movie, value in mlist1.items():
        cast = get_actors(value)
        for person in cast:
            if person['name'] == a2:
                continue
            person_movies = get_movies(person['name'])
            result = compare(person_movies, mlist2, person['name'], a2)
            if result is not False:
                lev1 = {"name1": a1, 
                        "movie": [movie],
                        "name2": person['name'],
                        "error": False}
                r.append(lev1)
                r.append(result)
                return r


def compare(list_films, list_films2, name, a2):
    ''' Compare set of two movies and check if there is common element '''
    if set(list_films2.keys()) & set(list_films.keys()):
        results = list(set(list_films2.keys()).intersection(list_films.keys()))
        return {"name1": name, 
                 "movie": results,
                 "name2": a2,
                 "error": False}
    else:
        return (False)


def get_movies(actor):
    ''' 
        Function takes an actor name
        and returns all the movies the actors is in
    '''

    name = actor.replace(" ", "+")
    print(name)
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
    return (list_films)

def get_actors(movie):
    ''' Make API call and return all the cast for a movie '''
    url = "http://www.theimdbapi.org/api/movie?movie_id={}".format(movie)
    results = requests.get(url)
    contents = results.json()['cast']
    return (contents)


if __name__ == "__main__":
    # call_api("brad pitt", "angelina jolie")
    # r = call_api("Meryl Streep","Daniel Day Lewis")
