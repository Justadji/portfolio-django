from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.models import CloudinaryField


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Oeuvre(models.Model):
    titre = models.CharField(max_length=200)
    image = CloudinaryField()
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
    image_reference = CloudinaryField(blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.nom} {self.prenom}, ({self.format}, {self.style})"


class PageAccueil(models.Model):
    titre_slide_1 = models.CharField(max_length=200, default="Offrez-vous un portrait d’exception")
    texte_slide_1 = models.TextField(default="Des œuvres uniques réalisées à la main.")
    titre_slide_2 = models.CharField(max_length=200, default="Des portraits faits avec passion")
    texte_slide_2 = models.TextField(default="Capturer l’essence de chaque regard.")
    
    image_accueil = CloudinaryField('Image d\'accueil', blank=True, null=True)
    image_profil = CloudinaryField('Image de profil', blank=True, null=True)

    def __str__(self):
        return "Contenu de la page d’accueil"

        verbose_name_plural = "Contenus de la page d'accueil"

from django.db import models
from cloudinary.models import CloudinaryField

class PageContact(models.Model):
    titre = models.CharField(max_length=200, default="Contactez-moi")
    texte_intro = models.TextField(blank=True, null=True)
    image_contact = CloudinaryField('image', folder='contact_images')
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "Contenu page Contact"

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

class Testimonial(models.Model):
    nom = models.CharField(max_length=100)
    texte = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']  # Les plus récents en premier

    def __str__(self):
        return f"{self.nom} - {self.texte[:30]}..."

