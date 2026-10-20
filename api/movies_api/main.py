from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
from os import getenv, path
from fastapi import Header, Depends
from json import load, dump

#part 3
#2
load_dotenv(dotenv_path=Path('../../.venv/.env'))
API_KEY = getenv("API_KEY")
#3
def check_key(x_api_key: str | None = Header(default=None)):
    if API_KEY is None or x_api_key != API_KEY:
        raise HTTPException(status_code=401)


#part 1
#1
app = FastAPI()
filename = 'movies.json'

def load_movies():
    movies = [
        {"id": 1, "title": "Big Trouble In Little China", "director": "John Carpenter", "year": 1986},
        {"id": 2, "title": "Monty Python and the Holy Grail", "director": "Terry Gilliam, Terry Jones", "year": 1975},
        {"id": 3, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001},
        {"id": 4, "title": "Conan the Barbarian", "director": "John Milius", "year": 1982}]

    if path.isfile(filename):
        with open(filename) as f:
            movies = load(f)
    return movies

def save_movies():
    with open(filename, "w") as fp:
            dump(movies, fp)

movies = load_movies()

#@app.get("/movies")
#def get_movies():
#    return movies

#2
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie:
        return movie
    raise HTTPException(status_code=404, detail="movie not found")

#3
@app.get("/movies")
def get_movies(director: str = None, year: int = None):    
    if director and year:
        return [movie for movie in movies if director.lower() in movie["director"].lower() and movie["year"] == year]
    if director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    if year:
        return [movie for movie in movies if movie["year"] == year]
    return movies

#4
class Movie(BaseModel):
    title: str
    director: str
    year: int

@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_book(movie: Movie):
    new_id = max([m["id"] for m in movies], default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year}
    movies.append(new_movie)
    save_movies()
    return new_movie

#5
def find_movie(movie_id: int):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie:
        return movie
    raise HTTPException(status_code=404, detail="movie not found")

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    save_movies()
    return existing

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
    save_movies()

#deleting same twice: 404 movie not found

#Part 2
#1
class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_id: int, movie_update: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(movie_update.model_dump(exclude_unset=True))
    save_movies()
    return movie

#2
#ok

#3
#empty body = 200 ok (but no changes)
#id that does not exist = 404

#4
'''
PUT replaces the whole movie.
PATCH replaces only the given fields, useful if some existing movie needs one or more fields updated.
'''

#part 3
#5
#post without key = 401
#post with key = 201
#post with one wrong character = 401

#part 4
#4
'''
If two people write to the file at same time, it is possible that it transpires in order of:
1) person 1 reads all movies
2) person 2 reads all movies
3) person 1 changes something and writes all movies to file
4) person 2 changes something and writes all moves to file (but the changes from person 1 gets lost since person 2 didn't re-read the movies before saving it)
In reality you could for example queue changes rather than overwriting whole database and have server handle merging the data.
Alternatively you can have some sort of database lock, so to write data you first have to:
1) lock the database against writing for all except the current thread
2) read the data you are about to update
3) make the update and write the updated data
4) release the lock
In this case person 2 would not write data until the write from person 1 was complete and their lock released.
'''



