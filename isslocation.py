"""Queries the ISS API to determine its latitude and longitude"""

import requests
import datetime


def iss_data():
    """Queries the API"""
    api_url = "http://api.open-notify.org/iss-now.json"
    iss_data = requests.get(api_url).json()
    # Prints the returned ISS data
    utc_now = str(datetime.datetime.utcnow())
    return {
        "lat": round(float(iss_data["iss_position"]["latitude"]), 2),
        "long": round(float(iss_data["iss_position"]["longitude"]), 2),
        "date": utc_now[:10],
        "time": utc_now[11:19],
    }


if __name__ == "__main__":
    print(iss_data())
