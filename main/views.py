from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .forms import FeedbacksForm
from .models import Feedbacks, Articles


def home(request):
    articles = Articles.objects.order_by('-date')
    today = timezone.now().date()
    now = timezone.now()

    data = {'articles': articles, 'today': today, 'now': now}
    return render(request, 'main/home.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def feedback(request):

    allFeedbacks = Feedbacks.objects.all()

    if request.method == "POST":
        form = FeedbacksForm(request.POST)
        if form.is_valid():
            form.save()
            allFeedbacks = Feedbacks.objects.all()
            form = FeedbacksForm()
            data = {'form': FeedbacksForm(), 'Feedbacks': allFeedbacks}
        else:
            error = 'Ошибка, неверно введена почта!'
            data = {'form': form, 'error': error, 'Feedbacks': allFeedbacks}

    else:
        form = FeedbacksForm()
        data = {'form': form, 'Feedbacks': allFeedbacks}

    return render(request, 'main/feedback.html', data)


def news(request, id):
    return HttpResponse(f"Статья {id}")