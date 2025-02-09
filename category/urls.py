from django.urls import path

from category.apps import CategoryConfig
from category.views import (CategoryListView, CategoryDetailView,
                            CategoryCreateView, CategoryUpdateView,
                            CategoryDeleteView)

app_name = CategoryConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('category_info/<int:pk>',
         CategoryDetailView.as_view(),
         name='category_info'),
    path('category_create/',
         CategoryCreateView.as_view(),
         name='category_create'),
    path('category_update/<int:pk>',
         CategoryUpdateView.as_view(),
         name='category_update'),
    path('category_delete/<int:pk>',
         CategoryDeleteView.as_view(),
         name='category_delete'),
]
