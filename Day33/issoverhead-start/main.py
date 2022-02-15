import time

import requests
from datetime import datetime

MY_LAT = 38.179306
MY_LONG = -85.723367

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise or time_now > sunset:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then email me to tell me to look up.
import smtplib


my_email = "someemail@provider.com"
my_password = "somepassword"

# while True:
#     # sleep for 60 seconds and execute code again
#     time.sleep(60)
#     # indent below code to execute every 60 seconds

if is_iss_overhead() and is_night():
    print("Look Up")


    # Uncomment the code below and fill in your Email info to get email sent to you
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #
    #     connection.starttls()
    #     connection.login(user=my_email, password=my_password)
    #     connection.sendmail(from_addr=my_email,
    #                         to_addrs=my_email,
    #                         msg="Subject:Look Up \n\nISS is Above you 👀☝️".encode("utf8"))

# BONUS: run the code every 60 seconds.



