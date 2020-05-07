# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    模拟异步存入样本读取样本
   Description :
   Author :       CBH
   date：         2020/4/30 15: 10
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/4/30 15: 10:
-------------------------------------------------
"""
import tensorflow as tf

#1.定义一个队列1000
Q = tf.FIFOQueue(1000,tf.float32)

#2.定义子线程要做的事   把值做处理 放入队列当中
var = tf.Variable(0.0)

#实现自增 tf.assign_add
data = tf.assign_add(var,tf.constant(1.0))
en_q = Q.enqueue(data)
#3.定义队列管理器op，指定子线程做什么，多少个子线程
qr = tf.train.QueueRunner(Q,enqueue_ops=[en_q] * 2)

#初始化变量op
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)

    #开启线程管理器
    cooard = tf.train.Coordinator()
    #真正开启子线程
    threds = qr.create_threads(sess,coord=cooard,start=True)

    #主线程，不断训练数据
    for i in range(300):
        print(sess.run(Q.dequeue()))

    #回收
    cooard.request_stop()
    cooard.join(threds)

