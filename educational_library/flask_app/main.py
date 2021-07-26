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
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# only run once to init database:
# db.create_all()


@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    import web

    app.register_blueprint(web.bp)

    import API

    app.register_blueprint(API.bp)

    app.run(host="0.0.0.0", debug=True)
