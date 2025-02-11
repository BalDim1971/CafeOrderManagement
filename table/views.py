"""
Вьюшка для просмотра столов
"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from table.forms import TableForm
from table.models import Table


class TableListView(ListView):
    model = Table
    template_name = 'table/table_list.html'
    extra_context = {
        'title': 'Список столов',
        'object_list': Table.objects.all()
    }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список столов'
        context['object_list'] = Table.objects.all()
        return context
    
    def get_queryset(self):
        return Table.objects.all()
    

class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('table:list')
    extra_context = {
        'title': 'Создать стол',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_table = form.save()
            new_table.slug = slugify(new_table.number)
            new_table.save()
        return super().form_valid(form)


class TableDetailView(DetailView):
    model = Table
    template_name = 'table/table_info.html'
    extra_context = {
        'title': 'Подробно о столе',
    }


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    success_url = reverse_lazy('table:list')
    extra_context = {
        'title': 'Обновить данные о столе',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class TableDeleteView(DeleteView):
    model = Table
    success_url = reverse_lazy('table:list')
    extra_context = {
        'title': 'Удалить стол',
    }
