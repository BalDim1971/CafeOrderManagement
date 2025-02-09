"""
Модель стола
"""
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Table(models.Model):
    """
    Модель стола
    1. number - номер стола,
    2. description - описание стола,
    3. image - изображение стола,
    4. count - количество посадочных мест около стола.
    """
    
    number = models.IntegerField(verbose_name='Номер стола', unique=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            validators=[
                                MinLengthValidator(1),
                                MaxLengthValidator(10),
                            ],
                            verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Описание стола')
    image = models.ImageField(upload_to='images/', default=None,
                              null=True, blank=True,
                              verbose_name="Изображение стола")
    count = models.IntegerField(verbose_name='Количество посадочных мест')
    
    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def get_absolute_url(self) -> str:
        return reverse(
            'table_detail',
            kwargs={'table_slug': self.slug}
        )

    def __str__(self) -> str:
        return (f"Cтол номер: {self.number} на {self.count} персон\n"
                f"Описание стола: {self.description}")
