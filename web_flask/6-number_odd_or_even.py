#!/usr/bin/python3
"""
Using flask to start a simple web server
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def num_check(n):
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_checker_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        text = f"{n} is even"
    else:
        text = f"{n} is odd"

    return render_template("6-number_odd_or_even.html", text=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
