# -*- coding: utf-8 -*-


class ValidateDB(object):
    def __init__(self):
        self.exists = 5

    # works like the defaultdict, the not exist attribute will be created
    # __getattribute__ will be called every time for any attribute
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            # super must be used in order to prevent infinitive loop
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

    def __getattr__(self, name):
        if name =='bad_name':
            raise AttributeError('%s is missing' % name)

data = ValidateDB()
print('exists:', data.exists)
print('foo:', data.foo)
print('foo:', hasattr(data, 'foo'))
print('bad_name:', hasattr(data, 'bad_name'))

