from django import forms

from .models import Pool

class CreatePoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['category', 'width', 'length', 'depth', 'decoration', 'additionally', 'desctiption']
        widgets = {
            'category': forms.RadioSelect(),
            'width': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Ширина'}),
            'length': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Длина'}),
            'depth': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Глубина'}),
            'decoration': forms.RadioSelect(),
            'additionally': forms.CheckboxSelectMultiple(),
            'desctiption': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Дополнительная информация'}),
        }
