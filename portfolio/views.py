from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import CommandeForm, ContactForm, ForumTopicForm, ForumPostForm, ForumReportForm, HoneypotForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Oeuvre, Commande, Categorie, PageAccueil, PageContact, Testimonial, ForumCategory, ForumTopic, ForumPost, ForumReport
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils import timezone

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
    if request.method == "POST":
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            commande = form.save()

            # Construire le message
            message = f"""
            Nouvelle commande reçue :
            Nom : {commande.nom}
            Prénom : {commande.prenom}
            Email : {commande.email}
            Format : {commande.format}
            Style : {commande.style}
            Description : {commande.description}

            Image de référence : {commande.image_reference.url if commande.image_reference else 'Aucune'}
            """

            send_mail(
                subject="Nouvelle commande de portrait",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["fullduerf0809@gmail.com"]
            )

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


def forum_index(request):
    categories = ForumCategory.objects.all()
    return render(request, 'forum_index.html', {'categories': categories})


def forum_category(request, categorie_id):
    categorie = get_object_or_404(ForumCategory, pk=categorie_id)
    topics = ForumTopic.objects.filter(categorie=categorie).order_by('-updated_at')

    topic_form = ForumTopicForm()

    if request.method == "POST":
        topic_form = ForumTopicForm(request.POST)
        if topic_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.categorie = categorie
            topic.save()

            return redirect('forum_topic', categorie_id=categorie.id, topic_id=topic.id)

    return render(request, 'forum_category.html', {
        'categorie': categorie,
        'topics': topics,
        'topic_form': topic_form,
    })


def forum_topic(request, categorie_id, topic_id):
    categorie = get_object_or_404(ForumCategory, pk=categorie_id)
    topic = get_object_or_404(ForumTopic, pk=topic_id, categorie=categorie)
    posts = ForumPost.objects.filter(topic=topic, parent__isnull=True).order_by('created_at')

    reply_form = ForumPostForm()
    if request.method == "POST":
        reply_form = ForumPostForm(request.POST)
        hp_form = HoneypotForm(request.POST)
        if reply_form.is_valid() and hp_form.is_valid() and not hp_form.cleaned_data.get("hp_field"):
            last_post_ts = request.session.get("forum_last_post_ts")
            now_ts = int(timezone.now().timestamp())
            if last_post_ts and now_ts - last_post_ts < 15:
                return redirect('forum_topic', categorie_id=categorie.id, topic_id=topic.id)
            reply = reply_form.save(commit=False)
            reply.topic = topic
            parent_id = request.POST.get("parent_id")
            if parent_id:
                reply.parent = get_object_or_404(ForumPost, pk=parent_id, topic=topic)
            reply.save()
            request.session["forum_last_post_ts"] = now_ts
            topic.updated_at = timezone.now()
            topic.save(update_fields=['updated_at'])
            return redirect('forum_topic', categorie_id=categorie.id, topic_id=topic.id)

    return render(request, 'forum_topic.html', {
        'categorie': categorie,
        'topic': topic,
        'posts': posts,
        'reply_form': reply_form,
        'report_form': ForumReportForm(),
    })


def forum_post_like(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    if not request.session.session_key:
        request.session.create()

    liked = request.session.get('liked_posts', [])
    if post_id not in liked:
        post.likes_count = post.likes_count + 1
        post.save(update_fields=['likes_count'])
        liked.append(post_id)
        request.session['liked_posts'] = liked

    return redirect('forum_topic', categorie_id=post.topic.categorie_id, topic_id=post.topic_id)


def forum_post_report(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    if request.method == "POST":
        form = ForumReportForm(request.POST)
        hp_form = HoneypotForm(request.POST)
        if form.is_valid() and hp_form.is_valid() and not hp_form.cleaned_data.get("hp_field"):
            last_report_ts = request.session.get("forum_last_report_ts")
            now_ts = int(timezone.now().timestamp())
            if last_report_ts and now_ts - last_report_ts < 30:
                return redirect('forum_topic', categorie_id=post.topic.categorie_id, topic_id=post.topic_id)
            report = form.save(commit=False)
            report.post = post
            report.save()
            request.session["forum_last_report_ts"] = now_ts
    return redirect('forum_topic', categorie_id=post.topic.categorie_id, topic_id=post.topic_id)

