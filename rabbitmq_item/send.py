#!/usr/bin/env python
# encoding: utf-8
'''
@file: send.py
@time: 2018/11/5 20:33
'''
import pika

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()

channel.queue_declare(queue='test')
channel.basic_publish(exchange='',routing_key='test',body='发送内容')
connection.close()



 