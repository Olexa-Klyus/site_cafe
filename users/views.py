from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('main_page:main_url'))
    else:
        form = UserLoginForm()

    context = {'form': form, 'title': 'Авторизація'}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = UserRegistrationForm

    context = {'form': form, 'title': 'Реєстрація'}
    return render(request, 'users/registration.html', context)


def profile(request):
    return render(request, 'users/profile.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('main_page:main_url'))
