#!/usr/bin/python3
"""
6th task file with a Flask app
"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """Root route that returns 'Hello HBNB!'

    Returns:
        str: returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Root route that returns 'HBNB!'

    Returns:
        str: returns 'HBNB!'
    """
    return "HBNB"


@app.route(f"/c/<text>")
def cisfun(text):
    """Root route that returns 'C <text>!'

    Returns:
        str: returns 'C <text>'
    """
    return "C {}".format(text.replace("_", " "))


@app.route(f"/python/", defaults={"text": "is so cool"})
@app.route(f"/python/<text>")
def python(text):
    """Root route that returns 'Python <text>! or Python is so cool'

    Returns:
        str: returns 'Python <text>! or Python is so cool'
    """
    return "Python {}".format(text.replace("_", " "))


@app.route(f"/number/<int:n>")
def number(n):
    """Root route that returns 'C <text>!'

    Returns:
        str: returns 'C <text>'
    """
    return f"{n} is a number"


@app.route(f"/number_template/<int:n>")
def number_template(n):
    """Root route that returns '<H1> tag and number!'

    Returns:
        str: returns '<H1> tag and number'
    """
    return render_template('5-number.html', n=n)


@app.route(f"/number_odd_or_even/<int:n>")
def odd_even_number(n):
    """Root route that returns '<H1> tag and number! if number odd or even'

    Returns:
        str: returns '<H1> tag and number! if number odd or even'
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
