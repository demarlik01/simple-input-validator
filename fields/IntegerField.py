from fields import Field


class IntegerField(Field):
    """
    IntegerField
    """
    def __init__(self, name, value):
        super(IntegerField, self).__init__(name, value)

    def check(self):
        if isinstance(self.value, int) is False:
            raise ValueError('Error %s is not int' % self.name)

    def validate(self):
        self.empty_check()
        self.check()
