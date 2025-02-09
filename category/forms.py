"""
Описание форм по работе с категориями блюд
"""

from django import forms

from category.models import Category


class CategoryForm(forms.ModelForm):
    """
    Форма для создания и редактирования категорий блюд
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Category
        fields = ('name', 'description', 'image')
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
