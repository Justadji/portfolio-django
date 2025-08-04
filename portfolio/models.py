from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Oeuvre(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='oeuvres/', storage=MediaCloudinaryStorage())
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.titre


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
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    format = models.CharField(max_length=10, choices=FORMATS, default="A4")
    style = models.CharField(max_length=20, choices=STYLES, default="Portrait")
    description = models.TextField(blank=True, null=True)
    image_reference = models.ImageField(upload_to='references/', blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.nom} {self.prenom}, ({self.format}, {self.style})"

