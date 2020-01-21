import os

print(__name__)
print(__package__)
# import sys
# _root = os.path.normpath("%s/.." % os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(_root)

import socket
import time
import random
from multiprocessing import Process
from threading import Thread
from .func_timer import TimeLogger

'''
Python中 time.sleep 是阻塞的，都知道使用它要谨慎，但在多线程编程中，time.sleep 并不会阻塞其他线程。
可以通过time sleep 模拟阻塞操作
'''


# 一个简单的同步socket应用
def blocking_way(number):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 向baidu主机的443端口发起网络连接请求 --> blocking
    sock.connect(('www.baidu.com', 443))
    time.sleep(random.random() * 3)  # 模拟耗时操作
    request = b'GET / HTTP/1.0\r\n Host: www.baidu.com\r\n\r\n'
    # sock.send()函数并不会阻塞太久，它只负责将请求数据拷贝到TCP/IP协议栈的系统缓冲区中就返回，并不等待服务端返回的应答确认。
    sock.send(request)
    response = b''
    # socket上读取4K字节数据 --> blocking
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    print('task {} end ({}) time: {}'.format(number, os.getpid(), time.time()))
    return response


# 同步方式(大约耗时13～17s)
@TimeLogger
def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way(i))
    return len(res)


@TimeLogger
def process_way():
    processes = []
    for i in range(10):
        p = Process(target=blocking_way, args=(i,))
        processes.append(p)
    for p in processes:
        p.start()
        # p.join()  # join() 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    for p in processes:
        p.join()
    return len(processes)


@TimeLogger
def threading_way():
    threads = []
    for i in range(10):
        p = Thread(target=blocking_way, args=(i,))
        threads.append(p)
    for t in threads:
        t.start()
        # t.join()
    for t in threads:
        t.join()
    return len(threads)

# sync_way()
# process_way()
# threading_way()

if __name__ == "__main__" and __package__ is None:
    __package__ = 'asynchronous'
    print(__name__)
    print(__package__)
    sync_way()
    process_way()
    threading_way()


# from .foo import a
#
# print('in main.py', __name__, __package__)
# print(a)

# if __name__ == "__main__":
#     print('in main.py', __name__)
#     print(a)
