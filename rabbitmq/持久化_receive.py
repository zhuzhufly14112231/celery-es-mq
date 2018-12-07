#!/usr/bin/env python
# encoding: utf-8
'''
@file: 持久化_receive.py
@time: 2018/11/5 11:19
'''
import pika

credentials = pika.PlainCredentials(username='root',password='123456')

conn = pika.ConnectionParameters(host='192.168.52.98',credentials=credentials)

connection = pika.BlockingConnection(conn)

# 建立管道
channel = connection.channel()

channel.queue_declare(queue='task_queue',durable=True)

def callback(ch,method,properties,body):
    print('receive %s' % body)
    # 手动对消息进行确认
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 保证能够做完之后通知给server端
channel.basic_qos(prefetch_count=1)
# no_ack默认为False,需要对message进行确认
channel.basic_consume(callback,queue='task_queue')

channel.start_consuming()



 