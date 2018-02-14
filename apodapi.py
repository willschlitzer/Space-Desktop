'''Queries the APOD API for the Astronomy Picture
of the Day and displays it'''

import requests

import urllib.request
from PIL import Image

import apodapi_config

apiurl = 'https://api.nasa.gov/planetary/apod?api_key=' + apodapi_config.apikey
apoddata = requests.get(apiurl).json()
imgurl = apoddata['hdurl']
file = urllib.request.urlretrieve(imgurl, 'apod.jpg')
image = Image.open('apod.jpg')
image.show()

