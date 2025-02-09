from django.urls import path

from orders.views import home_page

app_name = 'orders'

urlpatterns = [
    path('', home_page, name='home_page'),
]
