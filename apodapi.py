"""Queries the APOD API for the Astronomy Picture
of the Day, saves it, and displays it"""

import requests

import urllib.request
from PIL import Image

import api_config


def get_apod():
    """Retrieves and saves the APOD API"""
    api_url = 'https://api.nasa.gov/planetary/apod?api_key=' + api_config.nasaapikey
    apod_data = requests.get(api_url).json()
    # Saves the URL for the HD version of the APOD
    img_url = apod_data['hdurl']
    # Saves the APOD
    urllib.request.urlretrieve(img_url, 'apod.jpg')
    if __name__ == '__main__':
        image = Image.open('apod.jpg')
        image.show()
    return apod_data

if __name__ == '__main__':
    get_apod()