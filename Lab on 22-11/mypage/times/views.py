from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display_time(request):
    t=datetime.datetime.now()
    sc=f'<h1 style="text-align:center;background-color:#f0ad4e">Current Time : + {str(t)}</h1>'
    return HttpResponse(sc)
