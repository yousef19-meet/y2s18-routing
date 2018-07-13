from flask import Flask, render_template
app = Flask(__name__)

@app.route('/sum/???/???')
def hello_route(???):
    return render_template('sum.html', num1 = ???, num2 = ???, sum = ???)

app.run(debug=True)
