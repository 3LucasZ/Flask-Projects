from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 10)
print("Try to guess the number", number)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < number:
        return "<h1>Too low!</h1>"
    elif guess > number:
        return "<h1>Too high!</h1>"
    else:
        return "<h1>You got it!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
