#!/usr/bin/python3
"""
7th task file with a Flask app
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list")
def state_list():
    list_state = storage.all(State).values()
    states = sorted(list_state, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
