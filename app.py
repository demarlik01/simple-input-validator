# coding: utf-8
from flask import Flask
from flask import request
from functools import wraps
from validator import aValidator
app = Flask(__name__)


def validate(validator):
    def wrapper(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            print validator.check_required_names()
            print request.args
            return func(*args, **kwargs)
        return decorated_func
    return wrapper


@app.route("/")
@validate(validator=aValidator())
def hello():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
