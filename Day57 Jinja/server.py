import time
from random import randint
import requests
from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    current_year = time.localtime().tm_year
    return render_template("home.html", year=current_year)


@app.route('/guess/<name>')
def guess(name):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url)
    gender_data = response.json()
    gender = gender_data["gender"]
    url = f"https://api.agify.io?name={name}"
    response = requests.get(url)
    agify = response.json()
    age = agify["age"]
    return render_template("guesser.html", u_name=name, u_gender=gender, u_age=age)






if __name__ == "__main__":
    app.run(debug=True)

