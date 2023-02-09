from django.shortcuts import render
import random
# from django.http import HttpResponse
from .models import Category, Dish, Events, Gallery


def main(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)

    photos = list(Gallery.objects.filter(is_visible=True))
    random.shuffle(photos)
    gallery = photos[:8]
    # або можна
    # photos = list(Gallery.objects.all().order_by('?')[:8])

    events = Events.objects.filter(is_visible=True)

    # повертаємо за допомогою функції рендер через HTML файл (створили файл-шаблон menu.html в папці templates)
    # в context записуємо словник,до якого зможемо звертатися в шаблоні
    # return render(request, '', context={
    #     'categories': categories,
    # })
    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'events': events
    })

    # dishes = Dish.objects.all()
    # або просто повертаємо все як респонс
    # res1 = f"Categories - {'; '.join(map(str, categories))}"
    # res2 = f"Dishes - {'; '.join(map(str, dishes))}"
    # return HttpResponse(
    #     res1 + '    ///     ' + res2
    # )
