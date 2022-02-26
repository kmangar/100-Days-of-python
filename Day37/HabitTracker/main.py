import requests
import datetime
import os

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = os.environ["GRAPH_ID"]

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Coding",
    "unit": "Minute",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


TODAY = str(datetime.date.today()).replace("-","")
# BELOW code is valid aswell
# today = datetime.now()
# today.strftime("%Y%m%d")

# MINS = input("How many Mins did you code Today: ")
# print(TODAY)

# POST ing pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": TODAY,
    "quantity": input("How many Mins did you code Today?: ")
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


# UPDATE ing pixel,
# Uncomment update_config and response to Update the pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

# update_mins = str(int(input("What's the updated mins?: ")))


# update_config = {
#     "quantity": str(int(input("What's the updated mins?: ")))
# }

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# DELETE ing pixel

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
# response = requests.delete(url=delete_endpoint, headers=headers)
