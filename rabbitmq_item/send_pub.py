#!/usr/bin/env python
# encoding: utf-8
'''
@file: send_pub.py
@time: 2018/11/5 21:06
'''
import pika
cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()


 