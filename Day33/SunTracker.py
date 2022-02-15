import datetime

import requests


MY_LAT = 38.179306
MY_LNG = -85.723367

parameters ={
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"sunrise: {sunrise} \n"
      f"sunset: {sunset} \n"
      f"Current Time: {datetime.datetime.now().hour}")
