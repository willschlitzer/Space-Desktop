import requests
import json

def iss_data():
    apiurl = 'http://api.open-notify.org/iss-now.json'
    issdata = requests.get(apiurl).json()
    print(issdata)

if __name__ == '__main__':
    iss_data()
