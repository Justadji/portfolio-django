from django import forms
from .models import Commande, MessageContact

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message']


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

