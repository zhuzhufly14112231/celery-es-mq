#!/usr/bin/env python
# encoding: utf-8
'''
@file: direct_receive.py
@time: 2018/11/5 15:27
'''
import pika,sys

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()

channel.exchange_declare(exchange='direct_log',exchange_type='direct')

# 声明临时队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

routing_keys = sys.argv[1:]

for item in routing_keys:
    channel.queue_bind(exchange='direct_log',
                       queue=queue_name,
                       routing_key=item)

def callback(ch,method,properties,body):
    print('Receive %s:%s' % (method.routing_key,body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
