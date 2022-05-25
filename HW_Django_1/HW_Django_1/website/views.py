from django.shortcuts import render, redirect

from .forms import AddNewSaleForm
from .models import *


header_phones = [
    "+375 (17) 111-22-33",
    "+375 (29) 111-22-33",
]


def show_index(request):
    books_query = Books.objects.all()
    param_for_render = {
        'title': 'Главная страница',
        'header_phones': header_phones,
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


def show_sales(request):
    param_for_render = {
        'title': 'Обратная связь',
    }
    return render(request, 'website/sales.html', context=param_for_render)


def add_new_sale(request):
    """Форма: """
    if request.method == 'POST':  # пользователь нажал на кнопку добавить коммент
        adding_sales_form = AddNewSaleForm(request.POST, request.FILES)  # в этом объекте находятся данные, которые мы получили от пользователя из формы
        if adding_sales_form.is_valid():  # проверяем эти данные (пользователя) на корректность заполнения
            adding_sales_form.save()  # сохраняем данные, если они корректно заполнены
            return redirect('home')
    else:
        adding_sales_form = AddNewSaleForm()

    sales_list = Sales.objects.order_by('-time_create')

    param_for_render = {
        'adding_sales_form': adding_sales_form,
        'header_phones': header_phones,
        'sales_list': sales_list,
    }
    return render(request, 'website/sales.html', context=param_for_render)
