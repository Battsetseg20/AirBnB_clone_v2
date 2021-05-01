#!/usr/bin/python3
"""
Starts a Flask web application:
Web application must be listening on 0.0.0.0, port 5000
Routes:
     /: display “Hello HBNB!”
     /hbnb: display “HBNB”
     /c/<text>: Displays 'C' followed by the value of <text>.
     /python/(<text>): display “Python ”, followed by the
        value of the text variable (replace _ symbols with a space )
        The default value of text is “is cool”
Use the option strict_slashes=False in route def
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by <text>"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays Python followed by <text>"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
