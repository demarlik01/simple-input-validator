# coding: utf-8

from siv.validator import Validator
from siv.fields import IntegerField, StringField, FloatField, RegexField

EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

class SearchValidator(Validator):
    """
    example - SearchValidator
    """
    q = StringField(require=True, max_length=5)


class PostValidator(Validator):
    """
    post validator
    """
    post = StringField(require=True, min_length=1, max_length=10)


class RegisterValidator(Validator):
    """
    example
    """
    age = IntegerField(require=True)
    height = FloatField(min=10, max=300)
    name = StringField(max_length=5)
    mobile = IntegerField(max=5)
    email = RegexField(regex=EMAIL_REGEX, min_length=3, max_length=10)
