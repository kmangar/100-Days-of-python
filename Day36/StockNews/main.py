import datetime
import os

from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
# make this application work for multiple stocks simultaneously by changing the
# STOCK constant into a list of dictionaries called "stocklist":
#
# stock_list = [
#              {"symbol": "SQ", "name": "Square Inc"},
#              {"symbol": "TSLA", "name": "Tesla Inc"},
#              {"symbol": "NVDA", "name": "NVIDIA Corporation"}
#              ]
# take all the functional code and put it under a for loop, for stock in stock_list,
# where you replace STOCK_NAME and COMPANY_NAME usage with STOCK_NAME["symbol"] and COMPANY_NAME["name"].

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python
# dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)

stock_data = stock_response.json()["Time Series (Daily)"]
today = str(datetime.date.today())
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# Get the day before yesterday's closing stock price

two_days_ago_data = data_list[1]
two_days_ago_closing_price = two_days_ago_data["4. close"]
# print(two_days_ago_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint:
# https://www.w3schools.com/python/ref_func_abs.asp
difference = round(float(yesterday_closing_price) - float(two_days_ago_closing_price), 2)
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

# print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price
# the day before yesterday.
diff_percent = round(((difference / float(yesterday_closing_price)) * 100), 2)
abs_diff = abs(diff_percent)
# print(f"{diff_percent}%")

# If TODO4 percentage is greater than 5 then print("Get News").
if abs_diff > 4:
    # print("GET NEWS")
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "searchIn": "title",
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    # print(articles)

    # Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    recent_news = articles[:2]
    # print(recent_news)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_news = [f"HEADLINE: {article['title']} \nBRIEF: {article['description']}" for article in recent_news]
    print(formatted_news)

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, AUTH_TOKEN)

    for article in formatted_news:

        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_down}{abs(diff_percent)}% \n {article}",
            from_='+YOUR_TWILIO_NUMBER',
            to='+YOUR_PHONE_NUMBER'
        )
        # print(message.Status())
