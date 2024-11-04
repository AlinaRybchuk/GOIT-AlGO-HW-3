from django import forms
from .models import Author, Quote

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio'] 
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author']  
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}), 
        }