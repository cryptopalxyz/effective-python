# -*- coding: utf-8 -*-
import select
from threading import Thread
from time import time

# IO tensive task
# main process will stuck in the 'select' and cannot move forward
def slow_systemcall():
    select.select([],[],[],0.1)

start = time()
for _ in range(32):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start)) # Took 0.511 seconds


# use Threads
# it should run faster than above but it doesn't

start = time()
threads = []
for _ in range(32):
    thread = Thread(target=slow_systemcall())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start)) # Took 0.511 seconds
