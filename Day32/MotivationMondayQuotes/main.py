import smtplib
import datetime as dt
import random


MY_EMAIL = "someemail@provider.com"
MY_PASSWORD = "somepassword"


with open("quotes.txt") as file:
    # data = {author:text for (author, text) in file}
    data = file.read().split("\n")
    # print(data)


# gets the current day of the week Monday is 0
day_of_week = dt.datetime.now().weekday()


rn = random.choice(range(0, 101, 2))
random_quote = f"{data[rn]}\n{data[rn + 1]}"


if day_of_week == 0:
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation\n\n{random_quote}".encode("utf8"))


