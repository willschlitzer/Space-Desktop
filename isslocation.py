"""Queries the ISS API to determine its latitude and longitude"""

import requests
import datetime

def iss_data():
    """Queries the API"""
    apiurl = 'http://api.open-notify.org/iss-now.json'
    issdata = requests.get(apiurl).json()
    # Prints the returned ISS data
    return issdata, datetime.datetime.utcnow()

if __name__ == '__main__':
    print(iss_data())
