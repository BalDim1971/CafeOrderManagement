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
from django.utils import timezone
from pytils.translit import slugify

from dish.models import Dish
from table.models import Table


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

    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            validators=[
                                MinLengthValidator(5),
                                MaxLengthValidator(100),
                            ],
                            verbose_name='Slug')
    date = models.DateTimeField(verbose_name='Дата заказа',
                                default=timezone.now)
    time = models.TimeField(verbose_name='Время заказа',
                            default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='Сумма заказа')
    table_number = models.ForeignKey(Table,
                                     on_delete=models.PROTECT,
                                     related_name='table',
                                     verbose_name='Столы')
    items = models.ManyToManyField(to=Dish, verbose_name='Список блюд')
    status = models.CharField(max_length=7,
                              choices=STATUS_CHOICES,
                              default='pending',
                              verbose_name='Статус заказа')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-date', '-time']
        indexes = [
            models.Index(fields=['-date', '-time']),
        ]

    def __str__(self):
        return (f"Заказ #{self.id}. "
                f"Срок выполнения - {self.date} {self.time}."
                f"Сумма: {self.total_price}."
                f"Стол: {self.table_number.name}."
                f"Статус: {self.status}.")

    def get_absolute_url(self):
        return reverse("orders:order_detail", kwargs={
            "order_pk": self.pk
        })

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(str(self.date) + ' ' + str(self.time))
        return super().save(*args, **kwargs)
