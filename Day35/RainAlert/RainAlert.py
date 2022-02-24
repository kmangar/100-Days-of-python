import requests
import os
from twilio.rest import Client


account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

api_key = os.environ["API_KEY"]

# Below is coordinate for louisville, KY. HOWEVER, you can go to
# https://www.latlong.net/ and get your city coordinate 😁
latitude = 38.252666
longitude = -85.758453

# Parameters for the Open weather API call
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()

weather_info = response.json()

weather_today = weather_info["hourly"][:12]
weather_alerts = weather_info["alerts"]
alert_list = [alert["event"] for alert in weather_alerts]

will_rain = False

for hour_data in weather_today:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

# If it will rain use twilio to sent msg
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Hello\n\nIt's going to rain today Master. Remember to bring an ☔ \nalerts: {alert_list}️ \n-🤵",
        from_='+YOUR_TWILIO_NUMBER',
        to='+YOUR_PHONE_NUMBER'
    )
    print(message.status)

