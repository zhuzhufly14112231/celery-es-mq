#!/usr/bin/env python
# encoding: utf-8
'''
@file: receive_持久化.py
@time: 2018/11/5 21:01
'''
import pika
cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()
channel.queue_declare(queue='test',durable=True)
def callback(ch,method,props,body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='test')
channel.basic_consuming()
 