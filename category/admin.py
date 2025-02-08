"""
Файл админки для Категорий блюд.
"""

from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'image',)
    list_filter = ('name',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    
    @admin.display(description='Краткое описание')
    def description_info(self, category: Category) -> str:
        return f'Описание {len(category.description)} символов'
