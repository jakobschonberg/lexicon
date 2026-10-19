import os
from dotenv import load_dotenv
from api_client import get_json, get_request
from pathlib import Path
from re import sub
from time import sleep

#1
    #token created

#2
    #safely stored in .env

#3
dotenv_path = Path('../.venv/.env')
load_dotenv(dotenv_path=dotenv_path)
token = os.getenv("GITHUB_TOKEN")
headers = {'Authorization': f"Bearer {token}"}
user = input("get github repositary names of which user? ")
user = sub(r'[^a-zA-Z0-9\-\_]', '', user)
print(user)
response = get_json("http://api.github.com/users/" + user + "/repos", headers= headers, params= {"sort": "pushed, per_page=5"})
#print(response)

#4
sleep(0.2)
response = get_request("http://api.github.com/users/" + user + "/repos", headers= headers, params= {"sort": "pushed, per_page=5"})
#print(response.headers)
print(response.headers["X-RateLimit-Limit"])
  # limit is 5000
sleep(0.2)
response2 = get_request("http://api.github.com/users/" + user + "/repos", params= {"sort": "pushed, per_page=5"})
print(response2.headers["X-RateLimit-Limit"])
  # limit is 60

#5
  #The server said no: 401
    #api key didn't match any valid key so github api doesn't recognize us, so it's 401

#6
  #.env is not in the list, so all good

#7
  #token deleted
