from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'START HERE: CHANGE ME'

app.run(debug=True)
