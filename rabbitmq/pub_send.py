#!/usr/bin/env python
# encoding: utf-8
'''
@file: pub_send.py
@time: 2018/11/5 14:13
'''


import pika
import sys

cred = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()
# 有多个设备去连接到交换机,那么这个交换机把消息发送给哪个设备,
# 是根据交换机的类型决定的
# 交换机的类型: direct/topic/fanout
# fanout 这个类型是所有连接交换机的设备都收到消息,相当于广播
# 这里定义一个名称为logs的fanout类型的交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
print(sys.argv)
message = sys.argv[1] if len(sys.argv) > 1 else 'info:logs'

# 将消息发送到名为logs的交换机中
# 因为是fanout类型的交换机,所以不需要指定routing_key
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print('Sent %s' % message)
connection.close()





















































 