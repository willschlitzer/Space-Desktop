"""Queries the ISS API to determine its latitude and longitude"""

import requests
import datetime

def iss_data():
    """Queries the API"""
    apiurl = 'http://api.open-notify.org/iss-now.json'
    issdata = requests.get(apiurl).json()
    # Prints the returned ISS data
    utcnow = str(datetime.datetime.utcnow())
    return {'lat': round(float(issdata['iss_position']['latitude']),2),
            'long': round(float(issdata['iss_position']['longitude']),2),
            'date': utcnow[:10],
            'time': utcnow[11:19]}

if __name__ == '__main__':
    print(iss_data())
