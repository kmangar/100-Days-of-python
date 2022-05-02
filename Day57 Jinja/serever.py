import time
from genderize import Genderize
from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    current_year = time.localtime().tm_year
    return render_template("home.html", year=current_year)






if __name__ == "__main__":
    app.run(debug=True)

