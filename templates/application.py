from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello!"
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Good bye!"
    return render_template("index.html", headline=headline)
