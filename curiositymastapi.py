'''Queries the NASA API for the photos
from the Curiosity MASTCAM'''

import requests
import random


import urllib.request
from PIL import Image

import api_config

def mast_pic():
    sol = '1500'
    apiurl = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol='+ sol + '&camera=mast&api_key=' + api_config.nasaapikey
    curiositydata = requests.get(apiurl).json()
    key_list = []
    for key in curiositydata['photos']:
        key_list.append(key['img_src'])
    url = key_list[random.randint(1,len(key_list)-1)]
    urllib.request.urlretrieve(url, 'mastpic.jpg')
    image = Image.open('mastpic.jpg')
    #image.show()

if __name__ == '__main__':
    mast_pic()

