from django.contrib import admin
from .models import Oeuvre, Commande

admin.site.register(Oeuvre)
admin.site.register(Commande)

class OeuvreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_creation')
    list_filter = ('categorie',)
