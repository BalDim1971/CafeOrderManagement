"""
Файл моделей для категорий блюд.
Category - Категория блюд: название, описание, изображение.
"""

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Модель категории блюд
    1. name - название категории,
    2. slug - уникальный идентификатор категории,
    3. description - описание категории,
    4. image - изображение категории.
    """
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Категория блюд')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            validators=[
                                MinLengthValidator(5),
                                MaxLengthValidator(100),
                            ],
                            verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', default=None,
                              null=True, blank=True,
                              verbose_name="Изображение категории")
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self) -> str:
        return reverse(
            'category',
            kwargs={'cat_slug': self.slug}
        )

    def __str__(self) -> str:
        return (f"Наименование категории: {self.name}\n"
                f"Описание категории: {self.description}")
