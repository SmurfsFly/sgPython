#!/usr/bin/env python
# coding=utf-8
import time
import threading

def func(name, n):
    for i in range(n):
        print(name, i)
        time.sleep(0.5)
t1 = threading.Thread(target=func,args=('t1', 5))
t2 = threading.Thread(target=func,args=('t2', 10))
t3 = threading.Thread(target=func,args=('t3', 10))
print(t1.isDaemon())
t1.start()              #进程开始
#t1.join()               #等待线程t1结束，然后在执行主程序

t2.daemon = True        #随着主进程的消亡
t2.start()
print('t2  name :',t2.getName())            #获取线程t2设置名称
print('t2  setname :',t2.setName('TTTT2'))  #设置线程的名称
print('t2  name :',t2.getName())

t3.start()
print(t3.isAlive())                         #获取线程t3状态（是否存活）
#t1.join()
print("main end")



'''

func('t1')
func('t2')
func('t3')
print("over")
'''

