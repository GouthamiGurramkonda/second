from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jyothi(request):
    return HttpResponse('<h1>jyothi is a good girl</h1>')

def kamala(request):
    return HttpResponse('<h1>kamala is a developer</h1>')

def flower(request):
    return HttpResponse('<marquee><h1>girls likes me</h1></marquee>')
