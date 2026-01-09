from django.contrib import admin
from .models import (
    Categorie,
    Oeuvre,
    Commande,
    PageAccueil,
    PageContact,
    MessageContact,
    Testimonial,
)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(Oeuvre)
class OeuvreAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie")
    list_filter = ("categorie",)
    search_fields = ("titre", "description")


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "format", "style", "date_commande")
    list_filter = ("format", "style", "date_commande")
    search_fields = ("nom", "prenom", "email")


@admin.register(PageAccueil)
class PageAccueilAdmin(admin.ModelAdmin):
    list_display = ("titre_slide_1", "titre_slide_2")


@admin.register(PageContact)
class PageContactAdmin(admin.ModelAdmin):
    list_display = ("titre", "email", "telephone")
    search_fields = ("titre", "email", "telephone")


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_envoi")
    search_fields = ("nom", "email", "sujet", "message")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("nom", "date")
    search_fields = ("nom", "texte")


