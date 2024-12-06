#!python3
import requests
import json
from bs4 import BeautifulSoup

"""Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. We are going to
make use of the REQUESTS.Request method to retrieve this data and unpack it with json.loads into a variable that we can
use. Retrieve the data and present it in a more organized format. You may use text output or a window using Tkinter. Our
goal is to format the result in a reasonably organized format."""


'''
file3 = open(filename3,'r')
data3 = file3.read()
Numbers3 = json.loads(json.loads(data3))

print(Numbers3)
print(type(Numbers3))

import json
 
filename = 'facebook.txt' # html code

try:
    with open(filename3) as f:
        data = f.read()
    print("Data type before reconstruction : ", type(data))
 
    # reconstructing the data as a dictionary
    js = json.loads(data)
    print("Data type after reconstruction : ", type(js))
    print(js)
except Exception as e:
    print('Error msg: ', e)
    exit()
'''
req = requests.get('https://open-meteo.com/en/docs#latitude=49.2497&longitude=-123.1193')
file3 = req.text
soup = BeautifulSoup(file3, 'html.parser')

data = {
    "title": soup.h1.text if soup.h1 else None,
    "description": soup.find("p", class_="description").text if soup.find("p", class_="description") else None,
    "items": [li.text for li in soup.find_all("li")]
}

json_data = json.dumps(data, indent=4)
jsondata2 = json.loads(json_data)

for i in jsondata2:
    if i=='title':
        print('                  ',jsondata2[i],'\n')
    elif i=='items':
        print(i)
        for a in jsondata2[i]:
            print('    ',a)