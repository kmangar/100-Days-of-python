from flask import Flask
import random

app = Flask(__name__)
print(__name__)

def make_emphasis(*args):
    return f"<em>{args}<em>"


def make_bold(*args):
    return f"<b>{args}<b>"


def make_underlined(*args):
    return f"<u>{args}<u>"


@app.route("/")
def hellow_world():
    return "<h1 style='text-align: center'> Hello, World!</h1>" \
           "</p> This is a paragraph" \
           ""


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return"Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)



