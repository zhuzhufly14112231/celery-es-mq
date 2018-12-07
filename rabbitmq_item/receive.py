#!/usr/bin/env python
# encoding: utf-8
'''
@file: receive.py
@time: 2018/11/5 20:53
'''
import pika

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()
channel.queue_declare(queue='test')
def callback(ch,method,props,body):
    print(body)

channel.basic_consum(callback,no_ack=True,queue='test')
channel.start_consuming()


 