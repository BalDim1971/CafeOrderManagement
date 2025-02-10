"""
Описание форм по работе с блюдами
"""

from django import forms

from dish.models import Dish


class DishForm(forms.ModelForm):
    """
    Форма для создания и редактирования столов
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Dish
        fields = ('name', 'price', 'description', 'image', 'category')
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
