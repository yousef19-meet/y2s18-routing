from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# Class exercise: Add a route to /goodbye that says something.

# YOUR CODE HERE

app.run(debug=True)
