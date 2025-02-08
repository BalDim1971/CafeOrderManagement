"""
Вьюшка для просмотра Столов
"""

from django.shortcuts import render
from django.http import HttpResponse


def table(request: HttpResponse) -> HttpResponse:
    return HttpResponse("<h1>Здесь будет страница столов.</h1>")
