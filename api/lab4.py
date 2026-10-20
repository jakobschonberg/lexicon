from api_client import get_json
import json
from os import path, remove
from datetime import datetime, timedelta
from time import sleep

#1, #2
def get_wheather(city):
    filename = "response.json"
    data = ""
    response = {}

    if path.isfile(filename) and datetime.fromtimestamp(path.getctime(filename)) + timedelta(minutes=10) > datetime.now():
        with open(filename) as f:
            data = json.load(f)
    else:
        if path.isfile(filename):       
            remove(filename)
            sleep(30)
            #getctime bugs out if we don't sleep a long time before creating the file again. By bugging out I mean, it doesn't recognize the new file creation date and istead gives us the old creation date
            #possible workaround is getting the creation date by running the command dir or ls from windows shell and parsing the result
    cached_data = next((x for x in data if city.lower() == x["name"].lower()), None)
    if(cached_data):
        cache_list = []
        cache_list.append(cached_data)
        response["results"] = cache_list
        print("getting results from cached data")
    else:
        response = get_json("https://geocoding-api.open-meteo.com/v1/search", params = {"name": city, "count": 1})
    if "results" not in response.keys() or len(response["results"]) == 0:
        print("City not found") 
    else:        
        list_obj = None
        if path.isfile(filename) and datetime.fromtimestamp(path.getctime(filename)) + timedelta(minutes=10) > datetime.now():
            with open(filename, encoding="utf-8") as fp:
                list_obj = json.load(fp)
                
        if list_obj:
            list_obj.append(response["results"])
        else:
            list_obj = response["results"]
        with open("response.json", "w") as fp:
            json.dump(list_obj, fp)
        latitude = response["results"][0]["latitude"]
        longitude = response["results"][0]["longitude"]
        response2 = get_json("https://api.open-meteo.com/v1/forecast",
                            params = {"latitude": latitude, "longitude": longitude,
                                    "current": "temperature_2m,wind_speed_10m"})
        if "current" not in response2.keys():
            print("Could not find weather")
        else:
            temp = response2["current"]["temperature_2m"]
            temp_unit = response2["current_units"]["temperature_2m"]
            wind = response2["current"]["wind_speed_10m"]
            wind_unit = response2["current_units"]["wind_speed_10m"]
            city = response["results"][0]["name"]
            country = response["results"][0]["country"]
            print(f"{city}, {country}: {temp}{temp_unit}, wind {wind} {wind_unit}")

city = input("Which city? ")
get_wheather(city)

#3
'''
Caching can prevent api calls which can be useful to keep token usage and/or reduce the load
for the api server. Can also make repeat use of function faster since we don't call api.
'''