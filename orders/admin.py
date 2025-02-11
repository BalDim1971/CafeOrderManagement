"""
Файл админки для Категорий блюд.
"""

from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'total_price', 'table_number', 'status',)
    list_filter = ('date', 'time',)
    list_display_links = ('id', 'date', 'time',)
    search_fields = ('date', 'time', 'total_price', 'table_number', 'status',)
    prepopulated_fields = {'slug': ('date', 'time')}
    ordering = ('date', 'time',)
    
    @admin.display(description='Краткое описание')
    def description_info(self, order: Order) -> str:
        return f'Заказ {order.date} {order.time} на {order.total_price}'
