from django.contrib import admin
from .models import Category, Dish, Events, Gallery, Chefs, About, Whu_Us


# варіант адмінки на швидкоруч
# admin.site.register(Category)
# admin.site.register(Dish)

# варіант адмінки, щоб таблиця Dish була вкладена в Category(підпорядкована,вбудована)
# створюємо клас
class DishAdmin(admin.TabularInline):
    model = Dish
    # вказуємо поле привязки - спосок, в якому буде назва поля
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]

    # виводить в рядки в адмінці наступні поля
    list_display = ['title', 'position', 'is_visible']

    # дозволяє редагувати прямо в рядку наступні поля
    list_editable = ['position', 'is_visible']


# можна додати в адмінку таблицю dish ще раз як просту таблицю, а не підпорядковану

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish

    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc', 'price', 'photo']
    list_editable = ['position', 'is_visible', 'price']

    # можна додати панель фільтрів
    list_filter = ['category', 'is_visible']

    # якщо таблиця довга, розбити її на сторінки
    # list_per_page = 2


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery

    list_display = ['photo', 'is_visible', 'date_add', 'desc']
    list_editable = ['is_visible']
    list_filter = ['date_add']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events
    list_display = ['title', 'is_visible', 'price', 'desc_top']
    list_editable = ['is_visible', 'price', 'desc_top']


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    model = Chefs
    list_display = ['name', 'is_visible', 'specialty']
    list_editable = ['is_visible', 'specialty']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About


@admin.register(Whu_Us)
class Whu_UsAdmin(admin.ModelAdmin):
    model = Whu_Us
