from django.urls import path

from category.views import categories


urlpatterns = [
    path('', categories, name='categories'),
]
