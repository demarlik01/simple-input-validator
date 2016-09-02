# coding: utf-8

from flask import Flask
from siv import IntegerField, StringField
from siv import validate

from validator import registerValidator


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@validate(validator=registerValidator())
def hello():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
