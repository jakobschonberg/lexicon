from api_client import get_json
#1, #4
city = input("Which city? ")
response = get_json("https://geocoding-api.open-meteo.com/v1/search",
                       params = {"name": city, "count": 1})
#print(response)

if "results" not in response.keys() or len(response["results"]) == 0:
    print("City not found") 
else:
    latitude = response["results"][0]["latitude"]
    longitude = response["results"][0]["longitude"]
    print(latitude, longitude)

#2
    response2 = get_json("https://api.open-meteo.com/v1/forecast",
                        params = {"latitude": latitude, "longitude": longitude,
                                "current": "temperature_2m,wind_speed_10m"})
    #print(response2)
    '''
    {'latitude': 59.3289, 'longitude': 18.072357, 'generationtime_ms': 31.99613094329834, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 24.0,
    'current_units': {'time': 'iso8601', 'interval':'seconds', 'temperature_2m': '°C', 'wind_speed_10m': 'km/h'},
    'current': {'time': '2026-10-19T12:00', 'interval': 900, 'temperature_2m': 8.6, 'wind_speed_10m': 5.4}}
    '''

#3
    temp = response2["current"]["temperature_2m"]
    temp_unit = response2["current_units"]["temperature_2m"]
    wind = response2["current"]["wind_speed_10m"]
    wind_unit = response2["current_units"]["wind_speed_10m"]
    city = response["results"][0]["name"]
    country = response["results"][0]["country"]

    print(f"{city}, {country}: {temp}{temp_unit}, wind {wind} {wind_unit}")


