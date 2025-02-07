"""
Файл админки для Категорий блюд.
"""

from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'image',)
    list_filter = ('name',)
