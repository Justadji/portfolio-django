from django import forms
from .models import Commande

class CommandeForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20, required=False)
    description = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    sujet = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


