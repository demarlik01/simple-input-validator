#coding: utf-8

from functools import wraps
from flask import request

def validate(validator):
    def wrapper(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            validator.validate(request.args)
            return func(*args, **kwargs)
        return decorated_func
    return wrapper

