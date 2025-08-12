from django.contrib import admin
from .models import Oeuvre, Commande, PageAccueil, PageContact, MessageContact, Testimonial

admin.site.register(Oeuvre)
admin.site.register(Commande)
admin.site.register(PageAccueil)
admin.site.register(PageContact)
admin.site.register(MessageContact)

class OeuvreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_creation')
    list_filter = ('categorie',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("nom", "date")
    search_fields = ("nom", "texte")


