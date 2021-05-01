#!/usr/bin/python3
"""
Starts a Flask web aoolication
 Web application must be listening on 0.0.0.0, port 5000
 Routes: / and  display “Hello HBNB!”
 You must use the option strict_slashes=False in your route definition
"""
# import Flask class. An instance of this class will be our WSGI application.
from flask import Flask


# create an instance of this class.
app = Flask(__name__)


# use the route() decorator to tell Flask what URL should trigger our function
@app.route('/', strict_slashes=False)
# The function is given a name which is also used to generate URLs
#  for that particular function
def hello_hbnb():
    """ Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'
# If you have the debugger disabled or trust the users on your network,
# you can make the server publicly available simply by adding
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
