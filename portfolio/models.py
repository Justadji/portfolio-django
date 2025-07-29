from django.db import models

# galerie/models.py
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Oeuvre(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='oeuvres/')
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.titre

class Commande(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.date_commande.strftime('%d/%m/%Y')}"

FORMATS = [
    ('A4', 'A4 (21x29.7 cm)'),
    ('A3', 'A3 (29.7x42 cm)'),
    ('A2', 'A2 (42x59.4 cm)'),
]

STYLES = [
    ('portrait', 'Portrait'),
    ('dessin', 'Dessin'),
    ('croquis', 'Croquis'),
]

class Commande(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    format = models.CharField(max_length=10, choices=FORMATS, default="A4")
    style = models.CharField(max_length=20, choices=STYLES, default="Portrait")
    description = models.TextField(blank=True, null=True)
    image_reference = models.ImageField(upload_to='references/', blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.nom} ({self.format}, {self.style})"
