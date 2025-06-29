import requests
import json
import math
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
url = f'https://www.mapquestapi.com/directions/v2/route?key={api_key}'

origin =input("Origin (zip/postal code, address, etc): ")
destination =input("Destination (zip/postal code, address, etc): ")
# origin='T2H 2N1'
# destination='T2K 0G2'
'''

'''
headers={'Content-Type': 'application/json'}
params = {'key':api_key, }
body={
    'locations': [
        origin, destination
    ]
}

response = requests.post(url, headers=headers, json=body)
route = response.json()['route']
locations = route['locations']
distance = route['distance']
time = route['time']
formattedTime = route['formattedTime']
origin_obj = locations[0]
destination_obj = locations[1]

summary = (
    f"Origin: {origin_obj['adminArea6']} {origin_obj['adminArea6Type']} in {origin_obj['adminArea5']} {origin_obj['adminArea3']}\n"
    f"Destination: {destination_obj['adminArea6']} {destination_obj['adminArea6Type']} in {destination_obj['adminArea5']} {destination_obj['adminArea3']}\n"
    f"Distance: {distance}\n" 
    f"Distance in km: {distance * 1.60934}\n"
    f"Time in seconds: {time}\n"
    f"formattedTime: {formattedTime}\n"
)

print(summary)