"""
Вьюшка для просмотра категорий
"""

from django.shortcuts import render
from django.http import HttpResponse


def categories(request) -> HttpResponse:
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
