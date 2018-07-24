from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/hello')
@app.route('/hello/<string:name>')
def hello_route(name='Emily'):
    return render_template('hello.html', n=name)

# Class exercise:
#  - Add a route to /even_or_odd/<int:numr>
#  - Let number = int(num)
#  - If number is even, then return the template to
#    even_odd.html, with num=number and even_odd='even'
#  - Otherwise (if number is odd) return the template to
#    even_odd.html, with num=number and even_odd='odd'

# YOUR CODE HERE

app.run(debug=True)
