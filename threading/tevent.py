#!/usr/bin/env python
# coding=utf-8

import threading
import time
def worker(event, name):
    while not event.is_set():#这个事件是否被set
        print('({})waiting to test MySQL connect....'.format(name))#尝试连接数据库
        event.wait(1)    #等待线程结束（对其他线程进行阻塞状态）。另外，wait 里面还可以加入参数1，代表等待一秒（一秒的有效期）。
    print('({})MySQL  ready, now you can connect MySQL'.format(name))#数据库连接成功之后打印
    print('connected MySQL')

evt_mysql = threading.Event()#生成一个线程的对象
t1 = threading.Thread(target=worker, args=(evt_mysql, 't1'))                                            #实例化t1对象
t1.start()
t2 = threading.Thread(target=worker, args=(evt_mysql, 't2'))                                               
t2.start()

print('First of all, i am connecting mysql')
time.sleep(6)
print('ok')
evt_mysql.set()#连接上数据库之后 发送给wait信号，然后wait不再等待。继续执行数据库连接成功。

