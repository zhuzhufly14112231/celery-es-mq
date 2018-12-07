#!/usr/bin/env python
# encoding: utf-8
'''
@file: pub_receive.py
@time: 2018/11/5 14:32
'''
import pika

cred = pika.PlainCredentials(username='root', password='123456')
conn = pika.ConnectionParameters(host='192.168.52.98', credentials=cred)
connection = pika.BlockingConnection(conn)
channel = connection.channel()

# 这里需要和发送端保持一致
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 创建临时队列  消费者断开之后就自动删除
result = channel.queue_declare(exclusive=True)
# 取出临时队列的名字
queue_name = result.method.queue

# 将队列和交换机绑定一起
channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch,method,properties,body):
    print('receive %s' % body)

channel.basic_consume(callback,queue= queue_name,no_ack= True)
channel.start_consuming()

















