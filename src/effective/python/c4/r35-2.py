# -*- coding: utf-8 -*-

# annotate Field type with 'name' and 'internal_name'
class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    def __init__(self):
        # these will be assigned by metaclass
        self.name = None
        self.internal_name = None


class BetterCustomer(DatabaseRow):
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

foo = Customer()
print('Before: ', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Jerry'
print('After: ', repr(foo.first_name), foo.__dict__)

foo = BetterCustomer()
print('Before: ', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Jerry'
print('After: ', repr(foo.first_name), foo.__dict__)