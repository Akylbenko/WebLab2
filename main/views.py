from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def feedback(request):
    return render(request, 'main/feedback.html')

def news(request, id):
    return HttpResponse(f"Статья {id}")