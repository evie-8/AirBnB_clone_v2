#!/usr/bin/python3
"""using flask web framework"""


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """starting flask application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """second route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def replace(text):
    """Using variables"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def replace_text(text="is cool"):
    """Using variables"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """number variable"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number variable"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """number variable"""
    if isinstance(n, int):
        if n % 2 == 0:
            value = f"{n} is even"
        else:
            value = f"{n} is odd"
        return render_template("6-number_odd_or_even.html", value=value)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
