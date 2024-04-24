#!/usr/bin/python3
"""
9th task file with a Flask app
"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    list_state = storage.all(State).values()
    list_cities = storage.all(City).values()
    states = sorted(list_state, key=lambda state: state.name)
    cities = sorted(list_cities, key=lambda city: city.name)
    list_id = [state.id for state in states]
    return render_template("9-states.html", states=states,
                           cities=cities, value_id=id, list_id=list_id)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
