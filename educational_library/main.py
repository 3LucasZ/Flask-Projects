from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///educational-book-collection.db'
# remove the TRACK_MODIFICATIONS warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class EduBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# only run once to init database:
# db.create_all()


@app.route('/', methods=["GET"])
def home():
    return render_template("index.html", books_query=db.session.query(EduBook))


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = EduBook(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit', methods=["GET", "POST"])
def edit():
    # when form is sent back
    if request.method == "POST":
        book = EduBook.query.get(request.form['id'])
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    # when form is accessed
    # get  passed
    id = request.args.get('id')
    return render_template("edit.html", book=EduBook.query.get(id))


@app.route('/delete', methods=["GET"])
def delete():
    id = request.args.get('id')
    book = EduBook.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

