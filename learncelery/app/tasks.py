#!/usr/bin/env python
# encoding: utf-8
'''
@file: tasks.py
@time: 2018/11/6 14:39
'''

from __future__ import absolute_import
import time
from celery import shared_task

@shared_task
def add(x,y):
    time.sleep(1)
    return x+y

@shared_task
def mul(x,y):
    return x*y














 