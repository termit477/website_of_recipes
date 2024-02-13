from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .form import UserRegisterForm

# Create your views here.
def registration(request):
    title = 'Регистрация'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'Аккаунт сохранен'
    else:
        form = UserRegisterForm()
        message = 'Заполните форму'
    return render(request, 'registration/registration.html', {'form': form, 'message': message, 'title': title})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
