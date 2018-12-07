#!/usr/bin/env python
# encoding: utf-8
'''
@file: tasks.py
@time: 2018/11/6 16:57
'''

from __future__ import absolute_import
from django.core.mail import send_mail
from celery import shared_task
import logging

loger = logging.getLogger(__name__)

@shared_task
def celery_send_email(subject,message,from_email,recipient_list,**kwargs):
    try:
        loger.info('开始发送邮件')
        send_mail(subject,message,from_email,recipient_list,**kwargs)
        loger.info('发送邮件成功')
        return 'email_send_success!'
    except Exception as e:
        loger.info('email_send_error',e)


















 