#!/usr/bin/env python
# coding=utf-8
"""
生产者   消费者
"""
from threading import Thread,Condition
class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name = threadname)
    def run(self):
        global x
        con.acquire()                        #加锁
        if x == 100000000:
            con.wait()                       #等待
            pass
        else:
            for i in range(100000000):
                x += 1
            con.notify()                     #激活 
            print(x)
        con.release()                        #解锁

class Consumer(Thread):
    def __init__(self,threadname):
        Thread.__init__(self, name = threadname)

    def run(self):
        global x 
        con.acquire()
        if x == 0:
            con.wait()
            pass
        else:
            for i in range(100000000):
                x -= 1
            con.notify()
            print(x)
        con.release()


con = Condition()

x = 0
p = Producer('Producer')
c = Consumer('Consumer')

p.start()
p.join()
c.start()
c.join()

print(x)
