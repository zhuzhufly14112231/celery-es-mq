#!/usr/bin/env python
# encoding: utf-8
'''
@file: 持久化_send.py
@time: 2018/11/5 11:04
'''
import pika

credit = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=credit)
connection = pika.BlockingConnection(conn)

# 建立管道
channel = connection.channel()

# durable:server关闭了  队列依旧存在
channel.queue_declare(queue='task_queue',durable=True)

message = 'test chijiuhua'

# delivery_mode=2  消息持久化
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

print('Send done! %s' % message)
connection.close()
































 