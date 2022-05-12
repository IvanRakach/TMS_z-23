from django.shortcuts import render
from .models import *


def show_index(request):
    books_query = Books.objects.all()
    param_for_render = {
        'title': 'Главная страница',
        'books_query': books_query,
    }
    return render(request, 'website/index.html', context=param_for_render)


def show_about_us(request):
    param_for_render = {
        'title': 'О нас',
    }
    return render(request, 'website/about.html', context=param_for_render)


def show_feedback(request):
    param_for_render = {
        'title': 'Обратная связь',
    }
    return render(request, 'website/feedback.html', context=param_for_render)
