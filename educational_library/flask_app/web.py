from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from main import db, EduBook

bp = Blueprint('web', __name__, url_prefix='/web')


@bp.route('/all', methods=["GET"])
def get_all():
    return render_template("web/all.html", books_query=db.session.query(EduBook))


@bp.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = EduBook(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("web/add.html")


@bp.route('/edit', methods=["GET", "POST"])
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
    return render_template("web/edit.html", book=EduBook.query.get(id))


@bp.route('/delete', methods=["GET"])
def delete():
    id = request.args.get('id')
    book = EduBook.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))
