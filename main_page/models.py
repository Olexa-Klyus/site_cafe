import datetime
import os.path
import uuid

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    # щоб в адмінці відображалася назва категорії, потрібно реалізувати метод str
    def __str__(self):
        return f'{self.title}'

    # щоб в адмінці записи сортувалися, потрібно прописати списком або кортежем атрибути за якими сортуємо
    class Meta:
        ordering = ('position',)

    def __iter__(self):
        for item in self.dishes.all():
            yield item


class Dish(models.Model):
    # можна формувати за допогою модуля uuid нове коректне унікальне імя файла,
    # зберігаючи поточне розширення файлу
    # def get_file_name(self, file_name: str):
    #     ext = file_name.strip().split('.')[-1]
    #     new_name = f'{uuid.uuid4()}.{ext}'
    #     return os.path.join('dishes', new_name)

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    # upload_to присвоїти стрічку (назву папки)  додає підпапку, в якій будуть зберігатися фотки,
    # можна ще додати такий шаблон 'dishes/%y_%m_%d'- тоді буде створюватися папка, назва якої це поточна дата
    photo = models.ImageField(upload_to='dishes', blank=True)

    # або результат виконання функції, визначеної вище, яка буде формувати імя файла і яка повертає стрічку -
    # photo = models.ImageField(upload_to=get_file_name, blank=True)

    # якщо у форенкей додати related_name, то через нього можна доступитися до підпорядкованої таблиці
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')


#
class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery', blank=False)
    desc = models.CharField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)
    date_add = models.DateField(auto_now_add=True)


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True)
    desc_top = models.TextField(max_length=500, blank=True)
    desc_li_1 = models.CharField(max_length=100, blank=True)
    desc_li_2 = models.CharField(max_length=100, blank=True)
    desc_li_3 = models.CharField(max_length=100, blank=True)
    desc_bottom = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    photo = models.ImageField(upload_to='events', blank=True)

    def str(self):
        return f'{self.title}'


class Chefs(models.Model):
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='chefs', blank=True)
    is_visible = models.BooleanField(default=True)
    twitter = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    linkedin = models.CharField(max_length=30, blank=True)


class About(models.Model):
    video = models.CharField(max_length=100, blank=True)
    title_1 = models.CharField(max_length=50, unique=True)
    title_2 = models.CharField(max_length=50, unique=True)
    desc_top_1 = models.TextField(max_length=200, blank=True)
    desc_top_2 = models.TextField(max_length=200, blank=True)
    desc_li_1 = models.CharField(max_length=100, blank=True)
    desc_li_2 = models.CharField(max_length=100, blank=True)
    desc_li_3 = models.CharField(max_length=100, blank=True)
    desc_bottom = models.TextField(max_length=200, blank=True)

