#!/usr/bin/env python
# coding=utf-8

import subprocess
from threading import Thread
from queue import Queue
queue=Queue()
success = []
def run(i,q):
    while True:
        ip = q.get()
        print("Thread %s : Pinging: %s" % (i, ip))
        ret = subprocess.call('ping -c 1 %s' % ip,shell=True)
        if ret == 0:
            #print('%s:is alive'%ip)
            success.append(ip)
            print("网络状况良好")
        else:
            #print('%s:did not respond'%ip)
            print("网络不可达")
        q.task_done()
plist = []
#plist = ['172.25.2.123','172.25.2.34','172.25.2.89','172.25.2.7']
for i in range(1000):
    th = Thread(target=run, args=(i, queue))
    th.setDaemon(True)
    th.start()

for i in range(1,255):
    for j in range(1,254):

        plist.append('172.25.{}.{}'.format(i,j))

for ip in plist:
    queue.put(ip)

print("Main Thread waiting....")
queue.join()
print("Done")
print(success)
