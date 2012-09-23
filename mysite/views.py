__author__ = 'stim'
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("hello world")


def datetime1(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></hmtl>" % now
    return HttpResponse(html)