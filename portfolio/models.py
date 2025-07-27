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