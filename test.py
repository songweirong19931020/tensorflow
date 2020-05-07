# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    test
   Description :
   Author :       CBH
   date：         2020/4/29 16: 11
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/4/29 16: 11:
-------------------------------------------------
"""

import tensorflow as tf
import os
#定义命令行参数
#1.首先定义哪些参数需要在运行时指定
#2.程序当中获取命令行参数
#第一个参数：名字/默认值/说明
tf.app.flags.DEFINE_integer('max_step',100,'模型训练步数')
tf.app.flags.DEFINE_string('model_dir',' ','模型文件加载路径')
FLAG = tf.app.flags.FLAGS
def myregression():
    '''
    实现一个线性回归预测
    :return:
    '''
    with tf.variable_scope('data'):
        #1.准备数据，x 特征值 [100,1]   y目标值[100]
        x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name="x_data")
        #矩阵相乘必须是二维的
        y_true = tf.matmul(x,[[0.7]])+0.8
    with tf.variable_scope('model'):
        #建立线性回归模型，首先确定 特征和权重
        #随机初始化（给一个权重和偏执的值，让它取计算损失，然后再当前状态下优化）,用变量定义才能优化
        weight = tf.Variable(tf.random_normal([1,1],mean=0.0,stddev=1.0),name="w")
        bias = tf.Variable(0.0,name="b")
        #建立预测
        y_predict = tf.matmul(x,weight)+bias
    with tf.variable_scope('loss'):
        #3/建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true-y_predict))
    with tf.variable_scope('optimizer'):
        #优化损失，使用梯度下降 learning_rate: 0~1,2,3,5,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    #收集变量tensor
    tf.summary.scalar('losses',loss)
    tf.summary.histogram('weights',weight)
    #合并变量写入事件文件
    merged = tf.summary.merge_all()


    #定义初始化变量op
    init_op = tf.global_variables_initializer()

    #定义保存model实例
    saver = tf.train.Saver()

    #通过会话运行程序
    with tf.Session() as sess:
        #初始化变量
        sess.run(init_op)

        #打印最先初始化的权重和偏执
        print('随机初始化参数权重为：%f,偏执为：%f'%(weight.eval(),bias.eval()))
        #建立事件文件
        filewrite = tf.summary.FileWriter('./temp/',graph=sess.graph)

        #加载模型，覆盖模型中随即定义的参数从上次训练的参数结果开始
        if os.path.exists('./temp/ckpt/checkpoint'):
            saver.restore(sess,'./temp/ckpt/model')

        #循环训练，运行优化
        for i in range(1000):
            sess.run(train_op)
            #运行合并的tensor
            summary = sess.run(merged)
            filewrite.add_summary(summary,i)
            print('第%d参数权重为：%f,偏执为：%f' % (i,weight.eval(), bias.eval()))
        # saver.save(sess,'./temp/ckpt/model')
    return None





if __name__ == '__main__':
    myregression()