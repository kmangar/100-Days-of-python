

from flask import Flask
import random

app = Flask(__name__)
print(__name__)


@app.route("/")
def hellow_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/xUPJPBAdETrDmYJNXq/giphy.gif'>"


if __name__ == "__main__":
    app.run()





