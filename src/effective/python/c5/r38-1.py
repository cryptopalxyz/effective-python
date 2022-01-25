# -*- coding: utf-8 -*-
from threading import Thread


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from sensor
        counter.increment(1)

def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

how_many = 10**5 #100000, 10的5次方
print(how_many)
counter = Counter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %(5 * how_many, counter.count))
# Counter should be 500000, found 433191