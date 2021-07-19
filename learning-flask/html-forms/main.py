from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return render_template("form-output.html", name=name, password=password)
    else:
        return render_template("form-entry.html")


if __name__ == "__main__":
    app.run(debug=True)