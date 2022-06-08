from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)

app.secret_key = "some secret string"


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
