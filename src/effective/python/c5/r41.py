# -*- coding: utf-8 -*-
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import pool

from time import time


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


#Took 0.431 seconds

if __name__ == '__main__': # avoid concurrent.futures.process.BrokenProcessPool

    numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802),
               (19633109, 22653973), (20230677, 38141672), (15521645, 22296620), (20319045, 20210802),
               (19633209, 22659573), (20305677, 38141172), (15515645, 22279620), (20394045, 20202802)]
    start = time()
    result = list(map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start)) # Took 8.450 seconds

    start = time()
    pool = ProcessPoolExecutor(max_workers=4)
    result = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f secondss' % (end - start)) # Took 2.748 secondss



