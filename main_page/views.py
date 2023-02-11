from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Dish, Events, Gallery, Chefs, About, Whu_Us
from .forms import ReservationForm


def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    form_reserve = ReservationForm()

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    gallery = Gallery.objects.filter(is_visible=True).order_by('?')[:8]
    events = Events.objects.filter(is_visible=True)
    chefs = Chefs.objects.filter(is_visible=True)
    about = About.objects.get()
    whu_us = Whu_Us.objects.all()

    # повертаємо за допомогою функції рендер через HTML файл (створили файл-шаблон menu.html в папці templates)
    # в context записуємо словник,до якого зможемо звертатися в шаблоні
    # return render(request, '', context={
    #     'categories': categories,
    # })
    return render(request, 'main_page.html',
                  context={
                      'categories': categories,
                      'dishes': dishes,
                      'special_dishes': special_dishes,
                      'gallery': gallery,
                      'events': events,
                      'chefs': chefs,
                      'about': about,
                      'whu_us': whu_us,
                      'form_reserve': form_reserve
                  })

    # або як спрощений варіант - повертаємо все як респонс
    # res1 = f"Categories - {'; '.join(map(str, categories))}"
    # res2 = f"Dishes - {'; '.join(map(str, dishes))}"
    # return HttpResponse(
    #     res1 + '    ///     ' + res2
    # )
