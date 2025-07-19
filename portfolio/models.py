from django.db import models

class Oeuvre(models.Model):
    CATEGORIES = [
        ('portrait', 'Portrait'),
        ('paysage', 'Paysage'),
        ('abstrait', 'Abstrait'),
        ('autre', 'Autre'),
    ]
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='galerie/')
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='autre')
    date_creation = models.DateField(auto_now_add=True)

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


class Oeuvre(models.Model):
    CATEGORIES = [
        ('portrait', 'Portrait'),
        ('paysage', 'Paysage'),
        ('abstrait', 'Abstrait'),
        ('autre', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='oeuvres/')
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='autre')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


