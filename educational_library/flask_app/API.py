from flask import (
    Blueprint, render_template, redirect, request, url_for, jsonify
)
import random
from main import db, EduBook

bp = Blueprint('API', __name__, url_prefix='/api')


@bp.route('/', methods=["GET"])
def home():
    return render_template('API/api-welcome.html')


@bp.route('/all', methods=["GET"])
def get_all():
    books = db.session.query(EduBook).all()
    return jsonify(books=[book.to_dict() for book in books])


@bp.route('/random', methods=["GET"])
def get_random():
    books = db.session.query(EduBook).all()
    random_book = random.choice(books)
    return jsonify(book=random_book.to_dict())


@bp.route('/get', methods=["GET"])
def get():
    id = request.args.get('id')
    title = request.args.get('title')
    author = request.args.get('author')
    category = request.args.get('category')
    rating = request.args.get('rating')
    if id:
        book = db.session.query(EduBook).get(id).to_dict()
        return jsonify(book=book)
    if title:
        book = db.session.query(EduBook).filter_by(title=title).first()
        return jsonify(book=book.to_dict())
    if author:
        books = db.session.query(EduBook).filter_by(author=author)
        return jsonify(books=[book.to_dict() for book in books])
    if category:
        books = db.session.query(EduBook).filter_by(category=category)
        return jsonify(books=[book.to_dict() for book in books])
    if rating:
        books = db.session.query(EduBook).filter_by(rating=rating)
        return jsonify(books=[book.to_dict() for book in books])
    return jsonify(error={"Not Found": "Please make a get request with the proper args."}), 404

