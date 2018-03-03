'''Queries the APOD API for the Astronomy Picture
of the Day and displays it'''

import requests

import urllib.request
from PIL import Image

import api_config

def get_apod():
    apiurl = 'https://api.nasa.gov/planetary/apod?api_key=' + api_config.nasaapikey
    apoddata = requests.get(apiurl).json()
    imgurl = apoddata['hdurl']
    urllib.request.urlretrieve(imgurl, 'apod.jpg')
    image = Image.open('apod.jpg')
    image.show()
    return apoddata

if __name__ == '__main__':
    get_apod()

