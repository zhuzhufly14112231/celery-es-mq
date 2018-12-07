#!/usr/bin/env python
# encoding: utf-8
'''
@file: direct_send.py
@time: 2018/11/5 15:18
'''
import pika,sys

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()

# 创建一个exchange,名字叫direct_log,类型是direct
channel.exchange_declare(exchange='direct_log',
                         exchange_type='direct')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = 'log 2333'
channel.basic_publish(exchange='direct_log',
                      routing_key=routing_key,
                      body=message)

print('Sent %s:%s' % (routing_key,message))
connection.close()













 