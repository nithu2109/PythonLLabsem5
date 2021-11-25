from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    sr=f"<h1 style='text-align:center'>Hello World!</h1>"
    return HttpResponse(sr)