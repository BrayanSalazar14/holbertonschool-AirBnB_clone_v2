#!/usr/bin/python3
"""
8th task file with a Flask app
"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/cities_by_states")
def cities_list():
    list_state = storage.all(State).values()
    list_cities = storage.all(City).values()
    states = sorted(list_state, key=lambda state: state.name)
    cities = sorted(list_cities, key=lambda city: city.name)
    return render_template("8-cities_by_states.html",
                           cities=cities, states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
