# coding: utf-8

from flask import Flask, request
from example_validator import RegisterValidator

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    validator = RegisterValidator()
    if not validator.validate(request.args):
        return str(validator.error)
    return "success"

if __name__ == "__main__":
    app.run(debug=True)
