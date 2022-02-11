# # Gmail: smtp.gmail.com
# #
# # Hotmail: smtp.live.com
# #
# # Outlook: outlook.office365.com
# #
# # Yahoo: smtp.mail.yahoo.com

import smtplib
import os

my_email = "someemail@provider.com"
my_password = "somepassword"


with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg="Subject:HELLO \n\nThis is the body".encode("utf8"))
#     # Don't need to use the .close if you use the with to open smtplib
#     # connection.close()
#
#

# import datetime as dt
#
# # gets the current time
# now = dt.datetime.now()
# # gets the current year
# year = now.year
# # gets the current day of the week
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1999, month=2, day=15)




