# -*- coding: utf-8 -*-

import os
from threading import Thread



class GenericWorker(object):
    def __init__(self, input_data, result=0):
        self.input_data = input_data
        self.result = result
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_worker(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def __init__(self, input_data, result=0):
        super(LineCountWorker, self).__init__(result=result, input_data=input_data)

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_worker(input_class, config)
    return execute(workers)


config = {'data_dir': '.'}
result1 = mapreduce(LineCountWorker, PathInputData, config)

print('There are', result1, 'lines')

# what if other InputData and Worker class, need to rewrite generate_inputs, create_workers and mapreduce function.
