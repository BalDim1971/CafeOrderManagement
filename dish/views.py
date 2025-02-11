"""
Вьюшка для просмотра Блюд
"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from pytils.translit import slugify

from dish.forms import DishForm
from dish.models import Dish


class DishListView(ListView):
    model = Dish
    template_name = 'dish/dish_list.html'
    extra_context = {
        'title': 'Список блюд',
        'object_list': Dish.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список блюд'
        context['object_list'] = Dish.objects.all()
        return context

    def get_queryset(self):
        return Dish.objects.all()


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy('dish:list')
    extra_context = {
        'title': 'Создать блюдо',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_dish = form.save()
            new_dish.slug = slugify(new_dish.name)
            new_dish.save()
        return super().form_valid(form)


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish/dish_info.html'
    extra_context = {
        'title': 'Подробно о блюде',
    }


class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy('dish:list')
    extra_context = {
        'title': 'Обновить данные о блюде',
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy('dish:list')
    extra_context = {
        'title': 'Удалить блюдо',
    }
