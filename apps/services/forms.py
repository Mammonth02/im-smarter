from django import forms

from apps.services.models import ServiceType

class UpdateServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'