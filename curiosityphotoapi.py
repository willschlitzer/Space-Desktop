'''Queries the NASA API for the photos
from the Curiosity MASTCAM'''

import requests
import random


import urllib.request
from PIL import Image

import api_config

def curiosity_pic(cam):
    sol = '1500'
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
    api_url = 'https://mars-photos.herokuapp.com/api/v1/manifests/curiosity'
    manifest_data = requests.get(api_url).json()
    camera(manifest_data, manifest_data['photo_manifest']['max_sol'])

def camera(data,sol):
    print(sol)
    for dict in data['photo_manifest']['photos']:
        if dict['sol'] == sol:
            print(dict)
            cameras = dict['cameras']
    if 'MAST' in cameras:
        curiosity_pic('mast')
    elif 'NAVCAM' in cameras:
        curiosity_pic('navcam')
    elif 'CHEMCAM' in cameras:
        curiosity_pic('chemcam')
    else:
        cam = cameras[random.randint(0,len(cameras)-1)]
        curiosity_pic(cam.lower)
    
if __name__ == '__main__':
    get_sol()

