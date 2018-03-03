'''Queries the People in Space API for the current people in space'''

import requests

api_url = 'http://api.open-notify.org/astros.json'
astros_data = requests.get(api_url).json()
astros_number = astros_data['number']
print(astros_number)
astronauts = astros_data['people']
print('Astronaut\t\tCraft')
for i in astronauts:
    print(i['name'], '\t\t', i['craft'])
