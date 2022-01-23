# -*- coding: utf-8 -*-
import json


class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dump({'args:', self.args})


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })

    def __repr__(self):
        name = self.__class__.__name__
        args_str = ", ".join(str(x) for x in self.args)
        return f"{name}({args_str})"

registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

# without meta class
register_class(EvenBetterPoint2D)

point = EvenBetterPoint2D(5, 3)
print('Before: ', point)
data = point.serialize()
print('Serialized: ', data)
after = deserialize(data)
print('After: ', after)


class Point3D(BetterSerializable):
    def __int__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

# will throw error because register_class(Point3D) is not run
# with meta class, register_class will auto run
point = Point3D(5, 3)
print('Before: ', point)
data = point.serialize()
print('Serialized: ', data)
after = deserialize(data)
print('After: ', after)
