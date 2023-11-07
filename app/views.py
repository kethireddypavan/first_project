from django.shortcuts import render
from django.http import HttpResponse

def pavan(request):
    return HttpResponse('<h1><marquee>hi pavan how are you</marquee>')