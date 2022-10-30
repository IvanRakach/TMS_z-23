from django.shortcuts import render


def index(request):  # главная страница + форма обратной связи в футере

    param_for_render = {

        'title': 'Главная страница'
    }
    return render(request, 'shop/index.html', context=param_for_render)
