from django.urls import path

from .apps import DishConfig
from .views import DishListView, DishDetailView, DishCreateView, \
    DishUpdateView, DishDeleteView

app_name = DishConfig.name

urlpatterns = [
    path('', DishListView.as_view(), name='list'),
    path('dish_info/<int:pk>',
         DishDetailView.as_view(),
         name='dish_info'),
    path('dish_create/',
         DishCreateView.as_view(),
         name='dish_create'),
    path('dish_update/<int:pk>',
         DishUpdateView.as_view(),
         name='dish_update'),
    path('dish_delete/<int:pk>',
         DishDeleteView.as_view(),
         name='dish_delete'),
]
