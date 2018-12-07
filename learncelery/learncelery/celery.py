#!/usr/bin/env python
# encoding: utf-8
'''
@file: celery.py
@time: 2018/11/6 14:30
'''
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','learncelery.settings')
app = Celery('learncelery')

# CELERY作为前缀,在settings中去配置
app.config_from_object('django.conf:settings',namespace='CELERY')

# 到django的各个app下,自动的发现tasks.py任务脚本
app.autodiscover_tasks()















 