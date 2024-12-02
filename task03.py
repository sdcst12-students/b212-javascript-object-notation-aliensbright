#!python3
import requests
import json

"""Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to
make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can
use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter. Our
goal is to format the result in a reasonably organized format."""


params = {
    "latitude": 49.015427,
    "longitude": -123.075432, 
    "hourly": "temperature_2m"
}


req = requests.get("https://open-meteo.com/en/docs",params=params)


data = req.text
print("data=",data)

decoded = json.loads(data)

print(decoded)