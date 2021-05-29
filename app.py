"""
Prac 10 - Flask Project with Modifications
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=0):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"You inputted {celsius} Celsius which is {fahrenheit:.2f} Fahrenheit."


if __name__ == '__main__':
    app.run()
