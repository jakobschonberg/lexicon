from fastapi import FastAPI, HTTPException, Query, Path as FastApiPath
from pydantic import BaseModel, Field
from pydantic.types import StringConstraints
from typing import Annotated, Literal
from dotenv import load_dotenv
from pathlib import Path as pathlibPath
from os import getenv, path as osPath
from fastapi import Header, Depends
from json import load, dump

#uv run fastapi dev

#part 3
#2
load_dotenv(dotenv_path=pathlibPath('../../.venv/.env'))
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
        {"id": 1, "title": "Big Trouble In Little China", "director": "John Carpenter", "year": 1986, "rating": 0},
        {"id": 2, "title": "Monty Python and the Holy Grail", "director": "Terry Gilliam, Terry Jones", "year": 1975, "rating": 0},
        {"id": 3, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001, "rating": 0},
        {"id": 4, "title": "Conan the Barbarian", "director": "John Milius", "year": 1982, "rating": 0}]

    if osPath.isfile(filename):
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

def lowercase(obj):
    if type(obj) is str:
        return obj.lower()
    return obj

#2
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int = FastApiPath(gt=0)):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie:
        return movie
    raise HTTPException(status_code=404, detail="movie not found")

#3
@app.get("/movies")
def get_movies(director: str | None = Query(default=None, min_length=2),
               year: int | None = Query(default = None, ge=1888, le=2100),
               title: str | None = Query(default = None),
               sort_by: Literal["title", "year", "director"] = "title",
               order: Literal["asc", "desc"] = "asc",
               limit: int = Query(default=10, ge=1, le=100),
               offset: int = Query(default=0, ge=0)):
    rmovies = movies
    if director and year:
        rmovies = [movie for movie in movies if director.lower() in movie["director"].lower() and movie["year"] == year]
    elif director:
        rmovies = [movie for movie in movies if director.lower() in movie["director"].lower()]
    elif year:
        rmovies = [movie for movie in movies if movie["year"] == year]
    if title:
        rmovies = [movie for movie in movies if title.lower() in movie["title"].lower()]
    sorted_movies = sorted(rmovies, key=lambda m: lowercase(m[sort_by]), reverse=(order == "desc"))
    total = len(sorted_movies)
    page = sorted_movies[offset:offset + limit]
    return {"total": total, "limit": limit, "offset": offset, "movies": page}

#4
class Movie(BaseModel):
    title: Annotated[str, StringConstraints(strip_whitespace=True), Field(min_length=1, max_length=100)]    
    director: Annotated[str, StringConstraints(strip_whitespace=True), Field(max_length=100)]
    year: int = Field(ge=1888, le=2100)
    rating: float = Field(default= 0, ge=0, le=10)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Pulp Fiction",
                    "director": "Quentin Tarantino",
                    "year": 1994,
                    "rating": 8.8
                }
            ]
        }
    }


@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    new_id = max([m["id"] for m in movies], default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year, 'rating': movie.rating}
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
def replace_movie(movie: Movie, movie_id: int = FastApiPath(gt=0)):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    existing["rating"] = movie.rating
    save_movies()
    return existing

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int = FastApiPath(gt=0)):
    movie = find_movie(movie_id)
    movies.remove(movie)
    save_movies()

#deleting same twice: 404 movie not found

#Part 2
#1
class MovieUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    director: str | None = Field(default=None, max_length=100)
    year: int | None = Field(default=None, ge=1888, le=2100)
    rating: int | None = Field(default=None, ge=0, le=10)

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_update: MovieUpdate, movie_id: int = FastApiPath(gt=0)):
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

#Extra
#1.3
#loc[1] and msg both seem like relevant information to show user

#2.2
#movies/0 and movies/1 are not permitted values so they give 422, while movies/999 is permitted, but we don't have a movie_id 999 in the database (yet) so it gives 404

#2.3
#422. Year = 1500 says: "Input should be greater than or equal to 1888"
#year = abc says: "Input should be a valid integer, unable to parse string as an integer"

#2.4
#In docs it says maximum: 2100 minimum: 1888 right under the input field

#3.3
#422 "type":"literal_error" 'msg': "Input should be 'title', 'year' or 'director'"

#4.3
#every case is as expected, offset 100 gets empty list as expected since we have less than 100 movies