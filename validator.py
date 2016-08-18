# coding: utf-8

from fields import *

class Validator(object):
    """
    validator
    """
    inputs = None

    def __init__(self):
        pass

    def check_required_names(self):
        self.__dict__.keys()

    def valdate(self):
        print self


class aValidator(Validator):
    """
    test
    """
    age = IntegerField()
    name = StringField()
