# -*- coding: utf-8 -*-

def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' % (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n - 1))

fibonacci(3)
print(fibonacci)
help(fibonacci) # Help on function wrapper in module __main__: