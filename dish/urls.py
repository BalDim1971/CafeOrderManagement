from django.urls import path

from .views import dish

app_name = 'dish'

urlpatterns = [
    path('', dish, name='dish'),
]
