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

class CloseableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # cause the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

def download(item):
    pass

def upload(item):
    pass

def resize(item):
    pass

download_queue = CloseableQueue()
resize_queue = CloseableQueue()
upload_queue = CloseableQueue()
done_queue = CloseableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()

print(done_queue.qsize(), 'items finished')
