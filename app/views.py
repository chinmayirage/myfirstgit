from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(resquest):
    return HttpResponse('this is my first function')
def chinmayi(request):
    return HttpResponse ('<h1><marquee>chinmayi is brave girl</h1></marquee>')