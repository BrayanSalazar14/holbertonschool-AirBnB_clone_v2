#!/usr/bin/python3
"""
10th task file with a Flask app
"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/hbnb_filters")
def airbnb_clone():
    list_state = storage.all(State).values()
    list_cities = storage.all(City).values()
    list_amenities = storage.all(Amenity).values()
    states = sorted(list_state, key=lambda state: state.name)
    cities = sorted(list_cities, key=lambda city: city.name)
    amenities = sorted(list_amenities, key=lambda amenity: amenity.name)
    return render_template("10-hbnb_filters.html", states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
