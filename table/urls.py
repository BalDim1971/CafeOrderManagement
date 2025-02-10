from django.urls import path

from .apps import TableConfig
from .views import (TableListView, TableDetailView, TableCreateView,
                    TableUpdateView, TableDeleteView)

app_name = TableConfig.name

urlpatterns = [
    path('', TableListView.as_view(), name='list'),
    path('table_info/<int:pk>',
         TableDetailView.as_view(),
         name='table_info'),
    path('table_create/',
         TableCreateView.as_view(),
         name='table_create'),
    path('table_update/<int:pk>',
         TableUpdateView.as_view(),
         name='table_update'),
    path('table_delete/<int:pk>',
         TableDeleteView.as_view(),
         name='table_delete'),
]
