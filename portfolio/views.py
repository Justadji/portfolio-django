from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CommandeForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Oeuvre, Commande, Categorie
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')

def galerie(request):
    categorie_id = request.GET.get('categorie')
    categories = Categorie.objects.all()
    oeuvres = Oeuvre.objects.all()

    if categorie_id:
        oeuvres = oeuvres.filter(categorie_id=categorie_id)

    return render(request, 'galerie.html', {
        'oeuvres': oeuvres,
        'categories': categories,
        'categorie_selectionnee': int(categorie_id) if categorie_id else None
    })

def commander(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            Commande.objects.create(
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
                description=form.cleaned_data['description']
            )
            messages.success(request, "Votre commande a été enregistrée avec succès !")
            return redirect('commander')
    else:
        form = CommandeForm()
    return render(request, 'commander.html', {'form': form})


def contact(request):
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sujet = f"Message de {form.cleaned_data['nom']}"
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']
            destinataire = [settings.DEFAULT_FROM_EMAIL]

            send_mail(sujet, message, email_from, destinataire)
            success = True

    return render(request, 'contact.html', {'form': form, 'success': success})

def detail_oeuvre(request, pk):
    oeuvre = get_object_or_404(Oeuvre, pk=pk)
    return render(request, 'detail_oeuvre.html', {'oeuvre': oeuvre})


def galerie(request):
    categorie_id = request.GET.get('categorie')
    categories = Categorie.objects.all()

    if categorie_id:
        oeuvres = Oeuvre.objects.filter(categorie_id=categorie_id)
    else:
        oeuvres = Oeuvre.objects.all()
    try:
        categorie_active = int(categorie_id) if categorie_id else None
    except ValueError:
        categorie_active = None
    context = {
        'oeuvres': oeuvres,
        'categories': categories,
        'categorie_active': categorie_active,
    }
    return render(request, 'galerie.html', context)


def commander(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            # Tu peux enregistrer ou envoyer un email ici
            messages.success(request, "Votre commande a été envoyée avec succès !")
            return redirect('commander')
    else:
        form = CommandeForm()
    return render(request, 'commander.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            send_mail(
                f'Contact : {sujet} - {nom}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # À configurer
                fail_silently=False,
            )
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def oeuvre_detail(request, pk):
    oeuvre = get_object_or_404(Oeuvre, pk=pk)
    return render(request, 'oeuvre_detail.html', {'oeuvre': oeuvre})
