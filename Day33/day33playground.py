# import requests
# 
# response = requests.get("http://api.open-notify.org/iss-now.json")
# 
# response.raise_for_status()
# 
# data = response.json()
# 
# latitude = data["iss_position"]["latitude"]
# 
# longitude = data["iss_position"]["longitude"]
# 
# iss_position = (latitude, longitude)
# 
# print(iss_position)

# import requests
#
# response = requests.get("https://api.kanye.rest/")
#
# response.raise_for_status()
#
# quote = response.json()["quote"]
#
# print(quote)

import requests

# ?lat=36.7201600&lng=-4.4203400
MY_LAT = 38.192441
MY_LNG = -85.716705

parameters ={
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)


