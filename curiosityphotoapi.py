"""Queries the NASA API for the recent photos from Curiosity,
prioritizing the MASTCAM"""

import requests
import random

import urllib.request
from PIL import Image

import api_config

def curiosity_pic(cam, sol):
    api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol='+ sol + '&camera=' + cam + '&api_key=' + api_config.nasaapikey
    curiositydata = requests.get(api_url).json()
    key_list = []
    for key in curiositydata['photos']:
        key_list.append(key['img_src'])
    url = key_list[random.randint(1,len(key_list)-1)]
    urllib.request.urlretrieve(url, 'curiositypic.jpg')
    if __name__ == '__main__':
        image = Image.open('curiositypic.jpg')
        image.show()

def get_sol():
    """Queries the API for the maximum sol of Curiosity photos"""
    api_url = 'https://mars-photos.herokuapp.com/api/v1/manifests/curiosity'
    manifest_data = requests.get(api_url).json()
    camera(manifest_data, manifest_data['photo_manifest']['max_sol'])

def camera(data,sol):
    for datadict in data['photo_manifest']['photos']:
        if datadict['sol'] == sol:
            print(sol)
            print(datadict)
            cameras = datadict['cameras']
    sol = str(sol)
    if 'MAST' in cameras:
        curiosity_pic('mast', sol)
    elif 'NAVCAM' in cameras:
        curiosity_pic('navcam', sol)
    elif 'CHEMCAM' in cameras:
        curiosity_pic('chemcam', sol)
    else:
        cam = cameras[random.randint(0,len(cameras)-1)]
        curiosity_pic(cam.lower, sol)
    
if __name__ == '__main__':
    get_sol()

