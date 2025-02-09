"""
Настройки приложения Джанго для Категорий
"""

from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'category'
    verbose_name: str = 'Категории'
