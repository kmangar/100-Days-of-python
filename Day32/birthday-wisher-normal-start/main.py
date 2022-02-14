
import random

import pandas
from datetime import datetime
import smtplib

# Put it in the .env file for security
MY_EMAIL = "someemail@provider.com"
MY_PASSWORD = "somepassword"


today = datetime.now()
today_tuple = (today.month, today.day)


# pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")


# Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# dob_dict = {
#     (birthday_month, birthday_day): data_row
# }
dob_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# dob_dict = {
#     (12,21): test@email.com,1961,12,21
# }

# compare and see if today's month/day tuple matches one of the keys in dob_dict
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from
# letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# random module to get a number between 1-3 to pick a random letter.
# the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

if today_tuple in dob_dict:
    bp = dob_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as filereader:
        letter = filereader.read()
        letter = letter.replace("[NAME]", bp["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    # call .starttls()
    # login to your email service with email/password. Make sure your security setting is set to allow less secure apps.

    with smtplib ("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=bp["email"],
            msg=f"Subject:Happy Birthday!! \n\n{letter}"
        )





