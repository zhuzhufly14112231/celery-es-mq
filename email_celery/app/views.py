from django.shortcuts import render
from app.tasks import celery_send_email
from django.http import HttpResponse
# Create your views here.

def add_task_send_email(request):
    celery_send_email.delay('邮件的主题','晚上吃啥','17839211459@163.com',
                      ['1164984131@qq.com','17839211459@163.com','15138237961@163.com'])
    return HttpResponse('success')



























