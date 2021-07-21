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
