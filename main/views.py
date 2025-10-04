from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    return HttpResponse("<h1>Добро пожаловать в Новостной Блог!</h1>")
