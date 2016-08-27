# coding: utf-8

from flask import Flask
from validator import aValidator
from utils import validate
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@validate(validator=aValidator())
def hello():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
