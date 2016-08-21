# coding: utf-8

import inspect
from fields import *


class Validator(object):
    """
    validator
    """
    inputs = None

    def __init__(self):
        pass

    def check_required_names(self):
        print self.__dict__.keys()

    def set_values(self):
        members = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        attributes = [a for a in members if not(a[0].startswith('__') and a[0].endswith('__'))]
        print attributes        

    def valdate(self):
        print self


class aValidator(Validator):
    """
    test
    """
    age = IntegerField()
    name = StringField()
