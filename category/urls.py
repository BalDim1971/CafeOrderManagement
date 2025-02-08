from django.urls import path

from category.views import categories

app_name = 'category'

urlpatterns = [
    path('', categories, name='categories'),
]
