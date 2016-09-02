#coding: utf-8

from siv import Validator
from siv import IntegerField, StringField, IntegerField

class registerValidator(Validator):
    """
    example
    """
    age = IntegerField(require=True)
    name = StringField()
    mobile = IntegerField()
