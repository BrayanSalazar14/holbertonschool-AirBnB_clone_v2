#!/usr/bin/python3
"""
2th task file with a Flask app
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
