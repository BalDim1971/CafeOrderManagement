"""
Описание форм по работе с заказами
"""

from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    """
    Форма для создания и редактирования заказов
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ('date', 'time', 'table_number', 'items', 'status')
        exclude = ('slug',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'table_number': forms.Select(attrs={'class': 'form-control'}),
            'items': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
