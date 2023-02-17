from django.urls import path
from .views import main, update_reservation, list_reservation

app_name = 'main_page'

urlpatterns = [
    path('', main, name='main_url'),
    path('manager/update_reserve/<int:pk>', update_reservation, name='update_reservation'),
    path('manager/list_reserve', list_reservation, name='list_reservation'),
]
