# -*- coding: utf-8 -*-
from collections import deque
from threading import Thread, Lock
from time import sleep

"""
a. another loop to check if the done_queu has all items
b. cannot stop worker
c. incase any step gets delay, more data rushed in and caused the code to overflow
"""
# use Queue to fix this, queue.get will auto stuck, no need to check for IndexError

from queue import Queue
queue = Queue(1) #1 is the biggest pending task

def consumer():
    print('Consumer waiting')
    queue.get()
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object())
#thread.join() # can skip thread join, use task_done instead
print('Producer done')
queue.task_done()
