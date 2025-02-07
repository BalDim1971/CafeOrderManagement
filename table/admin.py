"""
Файл админки для Стола.
"""

from django.contrib import admin
from .models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'slug', 'description', 'image', 'count',)
    list_filter = ('number',)
    list_display_links = ('id', 'number')
    search_fields = ('number', 'description',)
    prepopulated_fields = {'slug': ('number',)}
    filter_vertical = ('number',)
    ordering = ('number',)
    
    @admin.display(description='Краткое описание')
    def description_info(self, table: Table) -> str:
        return f'Описание {len(table.description)} символов'
