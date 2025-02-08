"""
Вьюшка для просмотра Заказов
"""

from django.shortcuts import render
from django.http import HttpResponse


def orders(request) -> HttpResponse:
    return HttpResponse("<h1>Здесь будет страница заказов.</h1>")
