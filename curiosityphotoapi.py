"""Queries the NASA API for the recent photos from Curiosity"""

import requests
import random

import urllib.request
from PIL import Image

import api_config


def curiosity_pic(cam, sol, picname = 'curiositypic.jpg'):
    """Queries the API for the available photos, randomly selects and saves a photo, and opens it."""
    api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol='+ sol + '&camera=' + cam + '&api_key=' + api_config.nasaapikey
    curiositydata = requests.get(api_url).json()
    key_list = []
    # Appends key_list with the links to the images returned by the API
    for key in curiositydata['photos']:
        key_list.append(key['img_src'])
    # Randomly selects one of the photos returned
    url = key_list[random.randint(1,len(key_list)-1)]
    # Saves the selected photo
    urllib.request.urlretrieve(url, picname)
    if __name__ == '__main__':
        image = Image.open(picname)
        image.show()


def get_sol():
    """Queries the API for the maximum sol of Curiosity photos"""
    api_url = 'https://mars-photos.herokuapp.com/api/v1/manifests/curiosity'
    manifest_data = requests.get(api_url).json()
    # Determines the max sol from the .json data, passes to camera function
    return manifest_data, manifest_data['photo_manifest']['max_sol']


def camera(data, sol):
    """Determines the cameras used for the photos on the max sol"""
    for datadict in data['photo_manifest']['photos']:
        # Searches the data for the dictionary with the max sol
        if datadict['sol'] == sol:
            cameras = datadict['cameras']
    # Based upon the cameras returned for the max sol, returns the camera name
    if 'MAST' in cameras:
        return 'mast'
    elif 'NAVCAM' in cameras:
        return 'mast'
    elif 'FHAZ' in cameras:
        return 'fhaz'
    elif 'RHAZ' in cameras:
        return 'rhaz'
    elif 'MAHLI' in cameras:
        return 'mahli'
    elif 'CHEMCAM' in cameras:
        return 'chemcam'
    # Randomly selects a camera if there are no photos from the preferred cameras.
    else:
        cam = cameras[random.randint(0,len(cameras)-1)]
        return cam.lower()


def main():
    data, sol = get_sol()
    cam = camera(data, sol)
    sol = str(sol)
    curiosity_pic(cam, sol)
    return cam, sol


if __name__ == '__main__':
    main()
