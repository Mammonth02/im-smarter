from django import forms
from ckeditor.widgets import CKEditorWidget

from apps.shop.models import Category, Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget,
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Цена'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Kраткое описание'}),
        }

class CreateCatProductForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
        }