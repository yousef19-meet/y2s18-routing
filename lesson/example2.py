from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/hello/<string:name>')
def hello_route(name):
    return render_template('hello.html', n=name)

app.run(debug=True)
