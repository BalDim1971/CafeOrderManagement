"""
Вьюшка для просмотра категорий
"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from pytils.translit import slugify

from category.forms import CategoryForm
from category.models import Category


class CategoryListView(ListView):
    """
    Список категорий
    """
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'object_list'
    paginate_by = 3
    # extra_context = {
    #     'title': 'Список категорий товаров',
    #     'object_list': Category.objects.all()
    # }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий товаров'
        context['object_list'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        return Category.objects.all()
    

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    extra_context = {
        'title': 'Создать категорию товара',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_category = form.save()
            new_category.slug = slugify(new_category.name)
            new_category.save()
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_info.html'
    extra_context = {
        'title': 'Подробно о категории',
    }


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    extra_context = {
        'title': 'Обновить данные о категории',
    }
    
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.save()
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')
    extra_context = {
        'title': 'Удалить категорию',
    }
