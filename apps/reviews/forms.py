from django import forms
from .models import Reviews

class CreateReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating', 'text')

    