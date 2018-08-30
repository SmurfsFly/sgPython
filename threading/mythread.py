#!/usr/bin/env python
# coding=utf-8
import time
import threading

class MyThread(threading.Thread):
    def __init__(self, name):

        threading.Thread.__init__(self)
        self.name  = name

    def run(self):
        for i in range(10):
            print('this is {} {}'.format(i, self.name))
            time.sleep(0.5)
t1 = MyThread('t1')
t2 = MyThread('t2')
t3 = MyThread('t3')

t1.start()
t2.start()
t3.start()
print("main end")
