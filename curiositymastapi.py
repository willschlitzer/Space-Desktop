'''Queries the APOD API for the Astronomy Picture
of the Day and displays it'''

import requests
import random


import urllib.request
from PIL import Image

import api_config


#sol = str(random.randint(1500, 1750))
sol = '1500'
apiurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=' + sol + '&camera=mast&api_key=' + api_config.nasaapikey
curiositydata = requests.get(apiurl).json()
#print(curiositydata)
for key in curiositydata['photos']:
    print(key['img_src'])
#imgurl = apoddata['hdurl']
#urllib.request.urlretrieve(imgurl, 'apod.jpg')
#image = Image.open('apod.jpg')
#image.show()

