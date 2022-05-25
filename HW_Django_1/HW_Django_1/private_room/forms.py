from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-register',
                "placeholder": "Введите логин"}
        )
    )
    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-register',
                "placeholder": "Введите номер телефона"}
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control-register',
                "placeholder": "Введите email"}
        )
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control-register',
                "placeholder": "Введите пароль"}
        )
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control-register',
                "placeholder": "Подтвердите пароль"}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUSerForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control-login',
                'placeholder': 'Введите логин'}
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control-login',
                'placeholder': 'Введите пароль'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')
