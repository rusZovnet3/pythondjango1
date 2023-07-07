# libreria de django, metodo
from django.shortcuts import render, HttpResponse


class IndexController():
    def index(request, year):
        return HttpResponse('<h1>Carlos Fernando</h1>%s' % year)  #%s  formatea el dato int a str