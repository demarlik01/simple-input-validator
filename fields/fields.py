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
