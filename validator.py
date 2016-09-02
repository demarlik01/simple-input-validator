# coding: utf-8

import inspect
from fields import *


class Validator(object):
    """
    validator
    """

    def validate(self, inputs):
        members = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        attributes = [a for a in members if not(a[0].startswith('__') and a[0].endswith('__'))]
        required_keys = [attr[0] for attr in attributes if attr[1].require]

        if [r for r in required_keys if r not in inputs.keys()]:
            raise ValueError('required field not exsists')

        dict_attr = dict(attributes)
        for k in inputs.keys():
            dict_attr.get(k).name = k
            dict_attr.get(k).value = self.parse_to_numberic(inputs.get(k))

        for v in dict_attr.values():
            if v.value is not None:
                v.process()

    def parse_to_numberic(self, value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value


class aValidator(Validator):
    """
    test
    """
    age = IntegerField(require=True)
    name = StringField()
    mobile = IntegerField()
