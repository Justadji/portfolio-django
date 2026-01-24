from django import forms
from .models import Commande, MessageContact, ForumTopic, ForumPost

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


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['titre', 'auteur_nom', 'auteur_email']
        labels = {
            'titre': 'Titre du sujet',
            'auteur_nom': 'Votre nom',
            'auteur_email': 'Votre email (optionnel)',
        }


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['auteur_nom', 'auteur_email', 'message']
        labels = {
            'auteur_nom': 'Votre nom',
            'auteur_email': 'Votre email (optionnel)',
            'message': 'Message',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

