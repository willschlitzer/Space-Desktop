"""Queries the APOD API for the Astronomy Picture
of the Day, saves it, and displays it"""

import requests

import urllib.request
from PIL import Image

import api_config


def get_apod():
    """Retrieves and saves the APOD API"""
    apiurl = 'https://api.nasa.gov/planetary/apod?api_key=' + api_config.nasaapikey
    apoddata = requests.get(apiurl).json()
    # Saves the URL for the HD version of the APOD
    imgurl = apoddata['url']
    # Saves the APOD
    urllib.request.urlretrieve(imgurl, 'apod.jpg')
    if __name__ == '__main__':
        image = Image.open('apod.jpg')
        image.show()
    return apoddata

if __name__ == '__main__':
    get_apod()