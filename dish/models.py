"""
Модель блюда для заказов
Dish - Блюдо: имя, цена за единицу, возможно описание, фото, категория,
наличие или доступность.
"""

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from category.models import Category


class Dish(models.Model):
    """
    Модель блюда
    1. name - название блюда,
    2. price - цена за единицу,
    3. description - описание блюда,
    4. image - изображение блюда,
    5. category - категория блюда,
    6. is_available - доступность блюда,
    7. slug - ссылка на блюдо.
    """
    
    name = models.CharField(max_length=150, verbose_name="Название блюда")
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            validators=[
                                MinLengthValidator(5),
                                MaxLengthValidator(100),
                            ],
                            verbose_name='Slug')
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                verbose_name="Цена за единицу")
    description = models.TextField(verbose_name="Описание блюда")
    image = models.ImageField(upload_to='images/', default=None,
                              null=True, blank=True,
                              verbose_name="Изображение блюда")
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='dishes',
                                 verbose_name="Категории блюд")
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ('name',)
    
    def __str__(self) -> str:
        return (f"Название блюда: {self.name}\n"
                f"Цена за единицу: {self.price}\n"
                f"Описание блюда: {self.description}\n"
                f"Категория блюда: {self.category}\n"
                f"Доступность блюда: {self.is_available}")
    
    def get_absolute_url(self) -> str:
        return reverse(
            'dish',
            kwargs={'dish_slug': self.slug}
        )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
