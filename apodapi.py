'''Queries the APOD API for the Astronomy Picture
of the Day and displays it'''
import apodapi_config
import requests
import json
'''The APOD API URL is https://api.nasa.gov/planetary/apod?api_key=APIKEY'''
apiurl = apodapi_config.apiurl
apod_data = requests.get(apiurl).json()
#print(apod_data)
imgurl = apod_data['hdurl']
print(imgurl)
