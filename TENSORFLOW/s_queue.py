# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    queue
   Description :
   Author :       CBH
   date：         2020/4/30 14: 20
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/4/30 14: 20:
-------------------------------------------------
"""
import tensorflow as tf

#模拟同步处理数据，然后才能取数据训练

#1/确定图的结构,首先定义队列
Q = tf.FIFOQueue(3,tf.float32)

#放入一些数据
enq_many = Q.enqueue_many([[0.1,0.2,0.3],])

#2/定义读取数据，取数据过程  取数据，+1，入队列
out_q = Q.dequeue()

data = out_q+1

en_q = Q.enqueue(data)
with tf.Session() as sess:
    #初始化队列
    sess.run(enq_many)

    #处理数据
    for i in range(100):
        sess.run(en_q)

    #训练数据
    for i in range(Q.size().eval()):
        print(sess.run(Q.dequeue()))