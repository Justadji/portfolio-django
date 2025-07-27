from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def example_receiver(sender, instance, created, **kwargs):
    if created:
        print("Nouvel utilisateur créé :", instance.username)
