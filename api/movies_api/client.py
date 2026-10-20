from api_client import get_json
import requests

#6
BASE = 'http://127.0.0.1:8000'
movies = get_json(f"{BASE}/movies")
print(movies)
test404 = get_json(f"{BASE}/movies/99")
print(test404)

new_movie = {"title": "Avengers: Doomsday",
            "director": "Anthony Russo, Joe Russo",
            "year": 2026}

response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print(response.status_code, response.json())
