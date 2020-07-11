# -*- coding: utf-8 -*-
# Author:           Annihilation7
# Data:             2018-09-27
# Python version:   3.6

import sys
sys.path.append('../../')

import general_queue  # 普通队列在这个Py文件中
import loopqueue  # 循环队列在这个Py文件中
import numpy as np
import datetime
np.random.seed(7)


def count_time(func):

    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('共用时： %s 秒' % total_time)

    return int_time


generalQueue = general_queue.Queue()  # 普通队列对象
loopQueue = loopqueue.LoopQueue()  # 循环队列对象
nums = 30000  # 每个队列相应的操作次数


@count_time
def compute_generalQueue():
    global nums
    global generalQueue
    for i in range(nums):  # 入队30000次
        generalQueue.enqueue(np.random.randint(10))
    for i in range(nums):  # 出队30000次，这个很耗时间。。
        generalQueue.dequeue()


@count_time
def compute_loopQueue():
    global nums
    global loopQueue
    for i in range(nums):  # 同样的操作
        loopQueue.enqueue(np.random.randint(10))
    for i in range(nums):
        loopQueue.dequeue()


if __name__ == '__main__':
    print('普通队列：')
    compute_generalQueue()
    print('循环队列：')
    compute_loopQueue()
