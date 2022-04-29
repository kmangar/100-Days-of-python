from flask import Flask
import random

app = Flask(__name__)
print(__name__)

@app.route("/")
def hellow_world():
    return"Hello, World!"


@app.route("/bye")
def bye():
    return"Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)



