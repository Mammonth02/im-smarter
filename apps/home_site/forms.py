from django import forms

from apps.home_site.models import SiteInfo

class UpdateOrCreateInfoForm(forms.ModelForm):
    class Meta:
        model = SiteInfo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'working_time_start': forms.TimeInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'working_time_end': forms.TimeInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'adress': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Адрес'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название'}),
            'tw_link': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Твитер'}),
            'fe_link': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Фейсбук'}),
            'in_link': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Сайт'}),
            'sk_link': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Скайп'}),
        }