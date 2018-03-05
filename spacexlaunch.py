import requests

apiurl = 'https://api.spacexdata.com/v2/launches/upcoming'
spacexdata = requests.get(apiurl).json()
print(spacexdata)
