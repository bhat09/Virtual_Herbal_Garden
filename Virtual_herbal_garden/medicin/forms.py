from django import forms
from .models import Add_herb,ContactMessage,Remedy

class HerbForm(forms.ModelForm):
    class Meta:
        model = Add_herb
        fields = ["name", "description", "image"]  # Add fields based on your model

        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class RemedyForm(forms.ModelForm):
    class Meta:
        model = Remedy
        fields = ['disease', 'herbs']