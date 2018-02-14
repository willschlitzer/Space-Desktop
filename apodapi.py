'''Queries the APOD API for the Astronomy Picture
of the Day and displays it'''
import apodapi_config
import requests
import json
apiurl = 'https://api.nasa.gov/planetary/apod?api_key=' + apodapi_config.apikey
apod_data = requests.get(apiurl).json()
#print(apod_data)
imgurl = apod_data['hdurl']
print(imgurl)
