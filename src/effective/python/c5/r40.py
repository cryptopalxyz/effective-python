# -*- coding: utf-8 -*-

def my_coroutine():
    while True:
        received = yield
        print('Received:', received)

it = my_coroutine()
next(it) # prime the generator 使得generator起作用
it.send('First')
it.send('Second')
