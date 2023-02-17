from django.shortcuts import render, redirect
from .forms import UserRegistration, UserLogin
from django.contrib.auth import authenticate, login, logout


def registration_view(request):
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        # оскільки логін і пароль зберігаються в різних таблицях, для того щоб
        # записати дані в таблицю логінів спочатку отримуємо id з таблиці пасвордів
        # тобто спочатку пробний запис (commit=False)
        # потім валідація, якщо успіх - записуємо остаточно
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        return render(request, 'registration_done.html',
                      context={'user': new_user})

    return render(request, 'registration.html',
                  context={'form_registration': form})


# після авторизації повернути користувача на те місце, звідки він зайшов у авторизацію
def login_view(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # повертаємо аутифікованого юзера
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or '/')
    return render(request, 'log_in.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
