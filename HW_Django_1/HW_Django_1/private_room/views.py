from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from private_room.forms import LoginUSerForm, RegisterUserForm

header_phones = [
    "+375 (17) 111-22-33",
    "+375 (29) 111-22-33",
]


def show_private_room_page(request):

    param_for_render = {
        'header_phones': header_phones,
    }
    return render(request, 'private_room/private_room_home.html', context=param_for_render)


def register_user(request):

    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            if user_form.cleaned_data['password1'] == user_form.cleaned_data['password2']:
                new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
                new_user.save()
                return redirect('home')
    else:
        user_form = RegisterUserForm()

    param_for_render = {
        'user_form': user_form,
        'header_phones': header_phones,
    }
    return render(request, 'private_room/register_page.html', context=param_for_render)


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active and request.method == 'POST':
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        param_for_render = {
            'header_phones': header_phones,
        }
        return render(request, 'private_room/private_room_home.html', context=param_for_render)
    else:
        # Отображение страницы с ошибкой
        user_login_form = LoginUSerForm(request.POST)
        param_for_render = {
            'header_phones': header_phones,
            'user_login_form': user_login_form,
        }
        return render(request, 'private_room/login.html', context=param_for_render)


def logout_user(request):
    logout(request)  # logout - стандартная функция django
    return redirect('login')
