#!/usr/bin/env python
# coding=utf-8

import threading
import time
def worker(event, name):
    while not event.is_set():
        print('({})waiting to test MySQL connect....'.format(name))
        event.wait(1)
    print('({})MySQL  ready, now you can connect MySQL'.format(name))
    print('connected MySQL')


def event_sent(event, n):
    print('First of all, i am connecting mysql')
    time.sleep(n)
    event.set()
    print('over')
evt_mysql = threading.Event()
t1 = threading.Thread(target=worker, args=(evt_mysql, 't1'))    
t1.start()
t2 = threading.Thread(target=worker, args=(evt_mysql, 't2'))     
t2.start()
t3 = threading.Thread(target=event_sent, args=(evt_mysql, 3))     
t3.start()

