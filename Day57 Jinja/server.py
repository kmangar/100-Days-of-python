import string
import time
from random import *
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
    url = f"https://api.agify.io?name={name}"
    response = requests.get(url)
    agify = response.json()
    gender_set = ["male","female", "male","female", "female", "male","female", "male"]
    m_f = gender_data["gender"]

    if (not m_f or m_f == 'null'):
        m_f = choice(gender_set)

    ager = agify["age"]
    if ( not ager or ager == 'null'):
        ager = randint(13, 89)

    return render_template("guesser.html", u_name=name, u_gender=m_f, u_age=ager)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/0d3559339fd156af599c"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


