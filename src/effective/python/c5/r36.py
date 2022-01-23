# -*- coding: utf-8 -*-
import subprocess
from time import time

proc = subprocess.Popen(['echo', 'Hello from the child process!'], stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out.decode('utf-8'))

proc = subprocess.Popen(['echo', 'Hello from the child process!'], stdout=subprocess.PIPE)
# force to timeout with a very little time
out, err = proc.communicate(timeout=0.000000000001)
print(out.decode('utf-8'))

proc = subprocess.Popen(['sleep', '0.00000001'])
while proc.poll() is None:
    print('Working...')
print('Exit status', proc.poll())


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)
end = time()
print('Finished in %.3f seconds' % (end - start))