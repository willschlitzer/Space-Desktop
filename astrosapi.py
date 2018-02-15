'''Queries the People in Space API for the current people in space'''

import requests
import json

apiurl = 'http://api.open-notify.org/astros.json'
astrosdata = requests.get(apiurl).json()
astrosnumber = astrosdata['number']
print(astrosnumber)
astronauts = astrosdata['people']
print('Astronaut\t\tCraft')
for i in astronauts:
    print(i['name'],'\t\t',i['craft'])


