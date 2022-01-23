# -*- coding: utf-8 -*-

class LazyDB(object):
    def __init__(self):
        self.exists = 5

    # works like the defaultdict, the not exist attribute will be created
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo:', data.foo)
print('After:', data.__dict__)


class LoggingLazyDB(LazyDB):
    # only not exist attribute will call __getattr__
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print('Before:', data.__dict__)
print('foo:', data.foo)
print('foo:', data.foo)