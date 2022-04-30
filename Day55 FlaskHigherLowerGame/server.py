

from flask import Flask
import random

app = Flask(__name__)
print(__name__)

random_num = random.randrange(0,9)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/xUPJPBAdETrDmYJNXq/giphy.gif' width=200>"

@app.route("/<number>")
def guess(number):
    print(random_num)
    if int(number) < random_num:
        return "<h1>Too low, try again! </h1>" \
               "<img src='https://media.giphy.com/media/2uI9astifwiSUWVOTT/giphy.gif' width=200>"
    # https://media.giphy.com/media/JrqgYdYvUtHSjxKcSW/giphy.gif
    elif int(number) > random_num:
        return "<h1>Too high, try again! </h1>" \
               "<img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif' width=200>"
    else:
        return "<h1>You Guessed right</h1>" \
           "<img src='https://media.giphy.com/media/mbhseRYedlG5W/giphy.gif' width=200>"


if __name__ == "__main__":
    app.run()





