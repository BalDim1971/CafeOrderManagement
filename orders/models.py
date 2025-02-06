"""
Классы моделей для работы с заказами
1. Dish - Блюдо: имя, цена за единицу, возможно описание, фото, категория,
наличие или доступность.
2. Order - Заказ: дата, время, сумма, статус, список блюд,
возможность добавления комментария.
3. OrderItem - Блюдо в заказе: количество, цена, блюдо.
4. Comment - Комментарий к заказу: текст, дата, автор.
"""

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse

from dish.models import Dish


class Order(models.Model):
    """
    Модель заказа
    1. date - дата заказа,
    2. time - время заказа,
    3. total_price - общая сумма заказа,
    4. status - статус заказа,
    5. comment - комментарий к заказу,
    6. order_items - список блюд в заказе.
    """
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    time = models.TimeField(auto_now_add=True, verbose_name='Время заказа')
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='Сумма заказа')
