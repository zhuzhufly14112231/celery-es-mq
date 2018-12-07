from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import add
# Create your views here.



def add_view(request):
    add.delay(2,4)
    return HttpResponse('OK')














