#!/usr/bin/env python
# coding=utf-8
import time
from threading import Thread,RLock
class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name  = name
    def run(self):
        global x
        lock.acquire()                   #加锁
        for i in range(3):
            x += 1
        time.sleep(1)
        print('x= {}'.format(x))
        lock.release()                   #解锁
lock = RLock()
tl = []
for i in range(10):
    t = MyThread(str(i))
    tl.append(t)
x = 0
for i in tl:
    i.start()


