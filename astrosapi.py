'''Queries the People in Space API for the current people in space'''

import requests

def astros():
    """Queries the API"""
    api_url = 'http://api.open-notify.org/astros.json'
    astros_data = requests.get(api_url).json()
    # Saves and prints the number of people in space
    astros_number = astros_data['number']
    print(astros_number)
    astronauts = astros_data['people']
    # Prints the header for the table of astronauts and spacecraft
    print('Astronaut\t\tCraft')
    # Prints the fields of astronauts and their spacecraft
    for i in astronauts:
        print(i['name'], '\t\t', i['craft'])

if __name__ == '__main__':
    astros()
