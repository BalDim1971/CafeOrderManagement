"""
Вьюшка для просмотра Заказов
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed


def home_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает главную страницу приложения.
    Args:
        request: HttpRequest - Объект запроса Django.
    Returns:
        HttpResponse: Рендер шаблона главной страницы.
        HttpResponseNotAllowed: Если метод запроса не GET.
    """

    if request.method != "GET":
        return HttpResponseNotAllowed(permitted_methods=["GET"])

    return render(request, "orders/home_page.html")
