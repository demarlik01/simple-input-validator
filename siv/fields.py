# coding: utf-8
import sys
import re
import numbers

__all__ = [
    'Field',
    'NumbericField',
    'IntegerField',
    'FloatField',
    'StringField',
    'EmailField'
]


class Field(object):
    """
    Field
    - the base class of all Field classes

    """
    def __init__(self, name, value, require):
        self.name = name
        self.value = value
        self.require = require

    def check(self):
        pass

    def empty_check(self):
        if self.value is None:
            raise ValueError('Error: %s is None' % self.name)
        elif self.value == '':
            raise ValueError('Error: %s is empty' % self.name)

    def process(self):
        self.empty_check()
        self.check()


class NumbericField(Field):
    """
    NumbericField
    """
    def __init__(self, name=None, value=None, require=False, min=None, max=None):
        super(NumbericField, self).__init__(name, value, require)
        self.min = min
        self.max = max

    def check(self):
        if isinstance(self.value, numbers.Number) is False:
            raise ValueError('Error: %s is not number' % self.name)

    def range_check(self):
        if self.min and self.min > self.value:
            raise ValueError('Error: %s is too small' % self.name)

        if self.max and self.max < self.value:
            raise ValueError('Error: %s is too large' % self.name)

    def process(self):
        self.empty_check()
        self.check()
        self.range_check()


class IntegerField(NumbericField):
    """
    IntegerField
    """
    def __init__(self, name=None, value=None, require=False, min=None, max=None):
        super(IntegerField, self).__init__(name, value, require, min, max)

    def check(self):
        if isinstance(self.value, int) is False:
            raise ValueError('Error: %s is not int' % self.name)


class FloatField(NumbericField):
    """
    floatField
    """
    def __init__(self, name=None, value=None, require=False, min=None, max=None):
        super(FloatField, self).__init__(name, value, require, min, max)

    def check(self):
        if isinstance(self.value, float) is False:
            raise ValueError('Error: %s is not float' % self.name)


class StringField(Field):
    """
    StringField
    """
    def __init__(self, name=None, value=None, require=False, min_length=None, max_length=None):
        super(StringField, self).__init__(name, value, require)
        self.min_length = min_length
        self.max_length = max_length

    def is_string(self, string):
        if sys.version_info[0] < 3:
            return isinstance(self.value, basestring)
        return isinstance(self.value, str)

    def check(self):
        if self.is_string(self.value) is False:
            raise ValueError('Error: %s is not string' % self.name)

    def length_check(self):
        if self.min_length and len(self.value) < self.min_length:
            raise ValueError('Error: %s is too short' % self.name)

        if self.max_length and len(self.value) > self.max_length:
            raise ValueError('Error: %s is too long' % self.name)

    def process(self):
        self.empty_check()
        self.check()
        self.length_check()


class EmailField(StringField):
    """
    EmailField
    """
    email_regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    def __init__(self, name, value=None, requrie=False, min_length=None, max_length=None, email_regex=None):
        super(EmailField, self).__init__(name, value, requrie, min_length, max_length)
        if email_regex is not None:
            self.email_regex = email_regex

    def check(self):
        if re.match(self.email_regex, self.value) is None:
            raise ValueError('Error: %s is not email' % self.name)
