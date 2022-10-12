from django import forms

from .models import Additionally, Decoration, Pool, PoolCat

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

class CreateTypePoolForm(forms.ModelForm):
    class Meta:
        model = PoolCat
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'desctiption': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Описание'}),
        }

class CreatePoolAdditionallyForm(forms.ModelForm):
    class Meta:
        model = Additionally
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Описание'}),
        }

class CreatePoolDecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
        }