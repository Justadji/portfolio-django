from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import CommandeForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Oeuvre, Commande, Categorie, PageAccueil, PageContact, Testimonial
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def base(request):
    testimonials = Testimonial.objects.filter(visible=True)
    return render(request, 'base.html', {
        'testimonials': testimonials
    })

def home(request):
    contenu = PageAccueil.objects.first()
    return render(request, 'home.html', {
        'contenu': contenu,
    })


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

def contact(request):
    content = PageContact.objects.first()
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

    return render(request, 'contact.html', {'form': form, 'success': success, "content" : content})

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
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            style = form.cleaned_data['style']
            format = form.cleaned_data['format']
            description = form.cleaned_data['description']
            message = f"""
Nouvelle commande reçue :

Nom : {nom}
Prénom(s) : {prenom}
Email : {email}
Format souhaitée : {format}
style : {style}
Description : {description}
        """

            send_mail(
                'Nouvelle commande de portrait',
                message,
                settings.EMAIL_HOST_USER,
                ['fullduerf0809@gmail.com'], 
                fail_silently=False,
            )
            commande = form.save()
            envoyer_email_confirmation(commande)
            messages.success(request, "Votre commande a bien été envoyée.")
            return redirect("merci")
    else:
        form = CommandeForm()
    return render(request, 'commander.html', {'form': form})


def merci(request):
    return render(request, 'merci.html')


def contact(request):
    contenu = PageContact.objects.first()
    form = ContactForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        message_obj = form.save()

        # Envoi email
        send_mail(
            subject=message_obj.sujet,
            message=f"Message de {message_obj.nom} ({message_obj.email}):\n\n{message_obj.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contenu.email],
        )

        form = ContactForm()  # formulaire réinitialisé
        return redirect('contact_envoie')

    return render(request, 'contact.html', {
        'contenu': contenu,
        'form': form,
    })

def contact_envoie(request):
    return render(request, 'contact_envoie.html')

def oeuvre_detail(request, pk):
    oeuvre = get_object_or_404(Oeuvre, pk=pk)
    return render(request, 'oeuvre_detail.html', {'oeuvre': oeuvre})

def envoyer_email_confirmation(commande):
    subject = "Confirmation de votre commande de portrait"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [commande.email]
    #bcc = [settings.DEFAULT_FROM_EMAIL]

    context = {
        'prenom': commande.nom,
        'format': commande.format,
        'style': commande.style,
    }

    text_content = render_to_string("emails/confirmation.txt", context)
    html_content = render_to_string("emails/confirmation.html", context)

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()

