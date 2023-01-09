from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dab = SQLAlchemy(app)


class Book(dab.Model):
    __tablename__ = 'books'
    id = dab.Column(dab.Integer, primary_key=True)
    title = dab.Column(dab.String(250), unique=True, nullable=False)
    author = dab.Column(dab.String(250), nullable=False)
    rating = dab.Column(dab.Float, nullable=False)

with app.app_context():
    dab.create_all()


# class BookForm(FlaskForm):
#     BookName = StringField('Book name', validators=[DataRequired()])
#     Author = StringField('Name of Author:', validators=[DataRequired()])
#
#     Rating = SelectField(u'Coffee Rating',
#                          choices=[('📚'), ('📚', '📚'), ('📚', '📚', '📚'), ('📚', '📚', '📚', '📚'), ('📚', '📚', '📚', '📚', '📚')])
#
#     submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    all_books = dab.session.query(Book).all()

    return render_template('index.html', books=all_books, len=len)


@app.route("/add", methods=["GET", "POST"])
def add():
    # form = BookForm()
    if request.method == "POST":
        new_book = Book(
            title= request.form["title"],
            author= request.form["author"],
            rating= request.form["rating"]
        )
        dab.session.add(new_book)
        dab.session.commit()
        return redirect(url_for('home'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        dab.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

@app.route('/delete')
def delete():

    # UPDATE RECORD
    book_id = request.args.get('id')
    book_to_update = Book.query.get(book_id)
    dab.session.delete(book_to_update)
    dab.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
