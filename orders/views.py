"""
Вьюшки для просмотра Заказов
"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from pytils.translit import slugify

from orders.forms import OrderForm
from orders.models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    extra_context = {
        'title': 'Список заказов',
        'object_list': Order.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список заказов'
        context['object_list'] = Order.objects.all()
        return context

    def get_queryset(self):
        return Order.objects.all()


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order:list')
    extra_context = {
        'title': 'Создать заказ',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_order = form.save()
            new_order.slug = slugify(str(new_order.date) + ' ' + str(new_order.time))
            new_order.save()
        return super().form_valid(form)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_info.html'
    extra_context = {
        'title': 'Подробно о заказе',
    }


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order:list')
    extra_context = {
        'title': 'Обновить данные о заказе',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order:list')
    extra_context = {
        'title': 'Удалить заказ',
    }
