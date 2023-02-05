from django.shortcuts import render
# from django.http import HttpResponse
from .models import Category


def main(request):
    categories = Category.objects.all()
    # повертаємо за допомогою функції рендер через HTML файл (створили файл-шаблон menu.html в папці templates)
    # в context записуємо словник,до якого зможемо звертатися в шаблоні
    # return render(request, '', context={
    #     'categories': categories,
    # })
    return render(request, 'index.html', context={
        'categories': categories,
    })

    # dishes = Dish.objects.all()
    # або просто повертаємо все як респонс
    # res1 = f"Categories - {'; '.join(map(str, categories))}"
    # res2 = f"Dishes - {'; '.join(map(str, dishes))}"
    # return HttpResponse(
    #     res1 + '    ///     ' + res2
    # )

