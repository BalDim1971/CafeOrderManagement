"""
Вьюшка для просмотра Блюд
"""

from django.shortcuts import render
from django.http import HttpResponse


def dish(request: HttpResponse) -> HttpResponse:
    return HttpResponse("<h1>Здесь будет страница блюд.</h1>")
