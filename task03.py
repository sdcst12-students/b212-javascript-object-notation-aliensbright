#!python3
import requests
import json
import xmltojson 

"""Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to
make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can
use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter. Our
goal is to format the result in a reasonably organized format."""

"""
params = {
    "latitude": '49.015427',
    "longitude": '-123.075432', 
    "timezone": "America%2FLos_Angeles"
}
url='https://open-meteo.com/en/docs'

req = requests.get(url)
json_data = req.json()
print('hellow=',json_data)
data = req.text
#print("data=",data)
data03 = data.read()

decoded = json.loads(data03)

#print(decoded)"""

params1 = {
    "latitude": '49.015427',
    "longitude": '-123.075432', 
    "timezone": "America%2FLos_Angeles"
}

req = requests.post("https://open-meteo.com/en/docs",data=params1)
print(req)
json2 = json.dumps(req.text)
json3 = json.loads(json2)
print(type(json3),json3,json2)