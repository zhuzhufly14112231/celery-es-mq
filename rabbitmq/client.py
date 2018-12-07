#!/usr/bin/env python
# encoding: utf-8
'''
@file: client.py
@time: 2018/11/5 17:44
'''
import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        # 创建连接
        cred = pika.PlainCredentials(username='root', password='123456')
        conn = pika.ConnectionParameters(host='192.168.52.98', credentials=cred)
        self.connection = pika.BlockingConnection(conn)
        self.channel = self.connection.channel()

        # self.channel.queue_declare(queue='rpc_queue')
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        # 设置回调
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)


    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,n):
        # 设置响应和回调的通道id
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id),
                                   body=str(n))


        while self.response is None:
            self.connection.process_data_events()
        return self.response

fib = FibonacciRpcClient()
response = fib.call(20)
print(response)



















 