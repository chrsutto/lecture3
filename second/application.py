import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline ="Goodbye"
    return render_template("index.html", headline=headline)

@app.route("/newyear")
def nye():
    now = datetime.datetime.now()
    new_year = now.month == 5 and now.day == 30
    return render_template("nye.html", new_year=new_year)
