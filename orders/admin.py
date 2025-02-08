"""
Файл админки для Категорий блюд.
"""

from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'total_price', 'table', 'status',)
    list_filter = ('date', 'time',)
    list_display_links = ('id', 'date', 'time',)
    search_fields = ('date', 'time', 'total_price', 'table', 'status',)
    prepopulated_fields = {'slug': ('date', 'time')}
    ordering = ('date', 'time',)
