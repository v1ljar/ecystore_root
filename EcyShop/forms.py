from django import forms
from .models import Product


class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
