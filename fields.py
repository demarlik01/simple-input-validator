__all__ = (
    'Field',
    'IntegerField',
    'StringField',
    'FloatField'
)


class Field(object):
    """
    field
    """
    name = None
    value = None
    error = ""

    def __init__(self, name, value):
        self.name = name
        self.value = value
        # name : name of input key
        # value : value of input

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


class IntegerField(Field):
    """
    IntegerField
    """
    def __init__(self, name, value):
        super(IntegerField, self).__init__(name, value)

    def check(self):
        if isinstance(self.value, int) is False:
            raise ValueError('Error %s is not int' % self.name)


class StringField(Field):
    """
    StringField
    """
    def __init__(self, name, value):
        super(StringField, self).__init__(name, value)

    def is_string(self, string):
        import sys
        if sys.version_info[0] < 3:
            return isinstance(self.value, basestring)
        return isinstance(self.value, str)

    def check(self):
        if self.is_string(self.value) is False:
            raise ValueError('Error %s is not string' % self.name)


class FloatField(Field):
    """
    floatField
    """
    def __init__(self, name, value):
        super(FloatField, self).__init__(name, value)

    def check(self):
        if isinstance(self.value, float) is False:
            raise ValueError('Error %s is not float' % self.name)
