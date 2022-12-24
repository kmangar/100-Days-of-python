import csv

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []

class BookForm(FlaskForm):
    BookName = StringField('Book name', validators=[DataRequired()])
    Author = StringField('Name of Author:', validators=[DataRequired()])
    
    Rating = SelectField(u'Coffee Rating',
                         choices=[('📚'), ('📚', '📚'), ('📚', '📚', '📚'), ('📚', '📚', '📚', '📚'), ('📚', '📚', '📚', '📚', '📚')])
    
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html', books=all_books, len=len)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

