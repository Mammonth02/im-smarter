from django import forms
from .models import Reviews

class CreateReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating', 'text')
        widgets = {
                'rating': forms.RadioSelect(attrs={'class': 'bi bi-star'}),
                'text': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Отзыв'}),
            }