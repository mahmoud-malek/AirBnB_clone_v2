#!/usr/bin/python3

"""
 This is module to start a flask web applicaation
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloPage():
    """ a function to say hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnhPage():
    """ handler for hbnh page """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
