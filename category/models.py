"""
Файл моделей для категорий блюд.
Category - Категория блюд: название, описание, изображение.
"""

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


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
        ordering = ('name',)

    def get_absolute_url(self) -> str:
        return reverse(
            'category:category_info',
            args=[self.id]
        )

    def __str__(self) -> str:
        return f'{self.name} ({self.description})'
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
