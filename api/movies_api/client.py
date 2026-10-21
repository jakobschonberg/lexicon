from api_client import get_json, get_request
import requests
from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from math import ceil

#part1
#6
BASE = 'http://127.0.0.1:8000'
'''
movies = get_json(f"{BASE}/movies")
print(movies)
test404 = get_json(f"{BASE}/movies/99")
print(test404)

new_movie = {"title": "Avengers: Doomsday",
            "director": "Anthony Russo, Joe Russo",
            "year": 2026}

response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print(response.status_code, response.json())

#part3
#6
'''
load_dotenv(dotenv_path=Path('../../.venv/.env'))
API_KEY = getenv("API_KEY")
'''
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5, headers={"X-API-Key": API_KEY})
print(response.status_code, response.json())
'''
#401 without the api-key
#201 with the api-key

#7
#.env is not in the list = we're good

#extra
#4.4 - 5.4

def get_movies(api_key, limit = 10, page = 0, title = None, director = None, year = None, sort_by = "title", order = "asc"):    
    offset = page * limit
    url = f"{BASE}/movies?limit={limit}&offset={offset}"
    if title:
        url += f"&title={title}"
    if director:
        url += f"&director={director}"
    if year:
        url += f"&year={year}"
    if sort_by:        
        url += f"&sort_by={sort_by}"
    if order:
        url += f"&order={order}"    
    response = get_request(url, timeout=5, headers={"X-API-Key": api_key})
    if response.status_code == 200:
        json_response = response.json()
        if "movies" in json_response.keys():
            print(json_response)
            total_pages = ceil(json_response['total'] / limit)
            print(f"Page: {page+1} out of {total_pages}")
            for movie in json_response["movies"]:
                print(f"{movie['title']:<50} - {movie.get('rating', ''):<4} - {movie['year']} {movie['director']}")
        else:
            print("something went wrong")

get_movies(API_KEY, director = "li", order = "desc", sort_by="year", page=1, limit=2)

#4.5
#if someone deltes an item on page 1, the item that was previously the first item on page 2,
#would now be the last item on page 1. But if someone was already on page 1 and clicks next page,
#they might miss that item.

#5.3
#The 2 movies shown are no longer the 2 newest movies.
#Since we cut the unsorted movies down to 2 before sorting, it's whichever 2 movies were in those 2 positions
#Those 2 movies are then sorted between themselves so they appear in respective correct order relative to each other (but not the rest)
