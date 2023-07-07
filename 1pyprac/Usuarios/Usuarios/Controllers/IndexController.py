# libreria de django, metodo
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>Carlos Fernando</h1>')