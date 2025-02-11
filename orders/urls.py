from django.urls import path

from orders.apps import OrdersConfig
from orders.views import (OrderListView, OrderCreateView, OrderUpdateView,
                          OrderDeleteView, OrderDetailView)

app_name = OrdersConfig.name

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('order_info/<int:pk>',
         OrderDetailView.as_view(),
         name='order_info'),
    path('order_create/',
         OrderCreateView.as_view(),
         name='order_create'),
    path('order_update/<int:pk>',
         OrderUpdateView.as_view(),
         name='order_update'),
    path('order_delete/<int:pk>',
         OrderDeleteView.as_view(),
         name='order_delete'),
]
