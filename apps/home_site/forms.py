from django import forms
from ckeditor.widgets import CKEditorWidget

from apps.home_site.models import SiteInfo
from apps.shop.models import Category, Product
from apps.construction.models import Additionally, Decoration, PoolCat
from apps.services.models import ServiceType

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget,
        }

class CreateCatProductForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # widgets = {
        #     'content': CKEditorWidget,
        # }

class CreateTypePoolForm(forms.ModelForm):
    class Meta:
        model = PoolCat
        fields = '__all__'
        # widgets = {
        #     'content': CKEditorWidget,
        # }

class CreatePoolAdditionallyForm(forms.ModelForm):
    class Meta:
        model = Additionally
        fields = '__all__'
        # widgets = {
        #     'content': CKEditorWidget,
        # }

class CreatePoolDecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = '__all__'
        # widgets = {
        #     'content': CKEditorWidget,
        # }

class CreateServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'
        # widgets = {
        #     'content': CKEditorWidget,
        # }

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