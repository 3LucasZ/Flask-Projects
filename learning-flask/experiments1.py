from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold_wrapper():
        return "<b>" + function() + "</b>"
    return bold_wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>'


@app.route('/bye')
@make_bold
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
