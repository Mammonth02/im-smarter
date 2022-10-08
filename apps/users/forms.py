from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.users.models import Basket, User
from django.contrib.auth.forms import AuthenticationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Имя пользователя'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Подтверждение пароля '}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Адрес электронной почты'}),
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-label', 'placeholder': 'Имя пользователя'}),
            'password': forms.PasswordInput(attrs={'class': 'form-label', 'placeholder': 'Пароль'}),
        }

class CreateBasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('quantity', )

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'phone', 'address')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Имя пользователя'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Адрес электронной почты'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Номер'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Адрес'}),
        }