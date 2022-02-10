from unittest import mock
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
        widgets = {
            'name':forms.TextInput(attrs={'class':'formClass'}),
            'email':forms.EmailInput(attrs={'class':'formClass'}),
            'phone':forms.TextInput(attrs={'class':'formClass'}),
            'desc':forms.Textarea(attrs={'class':'desc formClass'}),
        }
        labels = {
            'name':'Full Name',
            'desc':'Description'
        }