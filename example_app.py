# coding: utf-8

from flask import Flask, request
from example_validator import SearchValidator
from example_validator import PostValidator
from example_validator import RegisterValidator
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    validator = SearchValidator()
    if not validator.validate(request.args):
        return str(validator.error)
    return "sucess"

@app.route("/post", methods=['POST'])
def post():
    validator = PostValidator()
    print request.form
    if not validator.validate(request.form):
        return str(validator.error)
    return "success"


@app.route("/join", methods=['POST'])
def join():
    validator = RegisterValidator()
    print request.get_json()
    json_dict = json.loads(request.data)
    print json_dict
    if not validator.validate(json_dict):
        return str(validator.error)
    return "success"



if __name__ == "__main__":
    app.run(debug=True)
