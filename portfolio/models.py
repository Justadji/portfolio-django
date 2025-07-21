from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Oeuvre(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='oeuvres/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='oeuvres')

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