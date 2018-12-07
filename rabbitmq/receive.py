#!/usr/bin/env python
# encoding: utf-8
'''
@file: receive.py
@time: 2018/11/5 10:22
'''
import pika

credentials = pika.PlainCredentials(username='root',password='123456')

conn = pika.ConnectionParameters(host='192.168.52.98',credentials=credentials)

connection = pika.BlockingConnection(conn)

channel = connection.channel()

# rabbitmq 消费端仍然使用此方法创建队列
# 这样做的意思就是:若没有就创建,目的是为了保证队列一定会有
channel.queue_declare(queue='hello')


def callback(ch,method,properties,body):
    print('Receive %s' % body)

# callback 回调函数 执行结束后立即执行的另一个函数
# no_ack 是否会告知服务端我是否收到消息,
#        True:对方没有收到消息的话不会将消息丢失,始终在队列里
channel.basic_consume(callback,
                     queue='hello',
                     no_ack=True)

print('Receive done!')
# 循环等待接收消息
channel.start_consuming()





























 