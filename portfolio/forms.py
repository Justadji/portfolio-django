from django import forms
from .models import Commande

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    sujet = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'prenom', 'email', 'format', 'style', 'description', 'image_reference']
        labels = {
            'nom': 'Nom(s)',
            'prenom' : 'Prénom(s)',
            'email': 'Adresse e-mail',
            'format': 'Format du portrait',
            'style': 'Style artistique',
            'description': 'Description / Instructions',
            'image_reference': 'Photo de référence',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

