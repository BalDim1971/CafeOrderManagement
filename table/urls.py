from django.urls import path

from .views import table

app_name = 'table'

urlpatterns = [
    path('', table, name='table'),
]
