from django import forms

from apps.services.models import ServiceType

class UpdateServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'

class CreateServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'desctiption': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Описание'}),
        }