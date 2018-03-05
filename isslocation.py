"""Queries the ISS API to determine its latitude and longitude"""

import requests
import json

def iss_data():
    """Queries the API"""
    apiurl = 'http://api.open-notify.org/iss-now.json'
    issdata = requests.get(apiurl).json()
    # Prints the returned ISS data
    print(issdata)

if __name__ == '__main__':
    iss_data()
