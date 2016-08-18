# coding: utf-8
import sys
import re
import numbers

__all__ = (
    'Field',
    'NumbericField',
    'IntegerField',
    'FloatField',
    'StringField',
    'EmailField'
)


class Field(object):
    """
    field
    """
    name = None
    require = None
    error = ""

    def __init__(self, name, require):
        self.name = name
        self.require = require
        # name : name of input key
        # value : value of input

    def check(self):
        pass

    def empty_check(self, value):
        if value is None:
            raise ValueError('Error: %s is None' % self.name)
        elif value == '':
            raise ValueError('Error: %s is empty' % self.name)

    def process(self, value):
        self.empty_check(value)
        self.check(value)


class NumbericField(Field):
    """
    NumbericField
    """
    min = None
    max = None

    def __init__(self, name=None, require=False, min=None, max=None):
        super(NumbericField, self).__init__(name, require)
        self.min = min
        self.max = max

    def check(self, value):
        if isinstance(value, numbers.Number) is False:
            raise ValueError('Error: %s is not number' % self.name)

    def range_check(self, value):
        if self.min and self.min > value:
            raise ValueError('Error: %s is too small' % self.name)

        if self.max and self.max < value:
            raise ValueError('Error: %s is too large' % self.name)

    def process(self, value):
        self.empty_check(value)
        self.check(value)
        self.range_check(value)


class IntegerField(NumbericField):
    """
    IntegerField
    """
    def __init__(self, name=None, require=False, min=None, max=None):
        super(IntegerField, self).__init__(name, require ,min, max)

    def check(self, value):
        if isinstance(value, int) is False:
            raise ValueError('Error %s is not int' % self.name)


class FloatField(NumbericField):
    """
    floatField
    """
    def __init__(self, name=None, require=False, min=None, max=None):
        super(FloatField, self).__init__(name, require, min, max)

    def check(self, value):
        if isinstance(value, float) is False:
            raise ValueError('Error %s is not float' % self.name)


class StringField(Field):
    """
    StringField
    """
    min_length = None
    max_length = None

    def __init__(self, name=None, require=False, min_length=None, max_length=None):
        super(StringField, self).__init__(name, value, require)
        self.min_length = min_length
        self.max_length = max_length

    def is_string(self, string):
        if sys.version_info[0] < 3:
            return isinstance(self.value, basestring)
        return isinstance(self.value, str)

    def check(self, value):
        if self.is_string(value) is False:
            raise ValueError('Error %s is not string' % self.name)

    def length_check(self):
        if self.min_length and len(self.value) < self.min_length:
            raise ValueError('Error %s is too short' % self.name)

        if self.max_length and len(self.value) > self.max_length:
            raise ValueError('Error %s is too long' % self.name)

    def process(self, value):
        self.empty_check()
        self.check()
        self.length_check()


class EmailField(StringField):
    """
    EmailField
    """
    email_regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    def __init__(self, name, value, requrie=False, min_length=None, max_length=None, email_regex=None):
        super(EmailField, self).__init__(name, value, requrie, min_length, max_length)
        if email_regex is not None:
            self.email_regex = email_regex

    def check(self):
        if re.match(self.email_regex, self.value) is None:
            raise ValueError('Error %s is not email' % self.name)