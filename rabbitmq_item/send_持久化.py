#!/usr/bin/env python
# encoding: utf-8
'''
@file: send_持久化.py
@time: 2018/11/5 20:58
'''
import pika

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()
channel.queue_declare(queue='test',durable=True)
channel.basic_publish(exchange='',routing_key='test',body='内容',properties=pika.BasicProperties(delivery_mode=2))
connection.close()

 