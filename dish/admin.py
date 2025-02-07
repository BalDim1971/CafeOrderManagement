"""
Админка для блюд
"""

from django.contrib import admin

from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'image', 'category',
                    'price',)
    list_filter = ('category', 'name', 'price',)
    list_display_links = ('id', 'name', 'price')
    list_editable = ('price',)
    search_fields = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    filter_vertical = ('category__name',)
    ordering = ('name', 'price')
    
    @admin.display(description='Краткое описание')
    def description_info(self, dish: Dish):
        return f'Описание {len(dish.description)} символов'
