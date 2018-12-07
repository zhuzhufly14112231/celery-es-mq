#!/usr/bin/env python
# encoding: utf-8
'''
@file: send.py
@time: 2018/11/5 9:19
'''
import pika

# 验证用户名和密码
credentials = pika.PlainCredentials(username='root',password='123456')

# 连接到队列服务器
# 这是通过远程连接到ip,要保证rabbitmq使用的端口是开放的
conn = pika.ConnectionParameters(host='192.168.52.98',credentials=credentials)

# 启用对库进行阻塞,同步操作进行简单的使用
connection = pika.BlockingConnection(conn)

# 声明一个管道
channel = connection.channel()

# 创建队列,设置队列的名字
# 如果rabbitmq服务器有队列那么就不管,如果没有就自动创建
channel.queue_declare(queue='hello')

# 使用默认的交换机发送信息,exchange为空就使用默认的
channel.basic_publish(exchange='',
                      # queue的名字,路由键,写明消息发往哪个队列
                      routing_key='hello',
                      # 消息的详细内容
                      body='server')

print("Send done! body=hello world!")
connection.close()































