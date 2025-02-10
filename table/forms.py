"""
Описание форм по работе со столами
"""

from django import forms

from table.models import Table


class TableForm(forms.ModelForm):
    """
    Форма для создания и редактирования столов
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Table
        fields = ('number', 'count', 'description', 'image')
        exclude = ('slug',)
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'couте': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
