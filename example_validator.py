# coding: utf-8

from siv.validator import Validator
from siv.fields import IntegerField, StringField


class RegisterValidator(Validator):
    """
    example
    """
    age = IntegerField(require=True)
    name = StringField(max_length=5)
    mobile = IntegerField(max=5)
