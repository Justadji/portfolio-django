from django.apps import AppConfig
import os

class PortfolioConfig(AppConfig):
    name = 'portfolio'
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        from django.contrib.auth.models import User
        if os.getenv('CREATE_SUPERUSER', 'False') == 'True':
            from django.db.utils import OperationalError
            try:
                if not User.objects.filter(is_superuser=True).exists():
                    User.objects.create_superuser(
                        username=os.getenv('DJANGO_SUPERUSER_USERNAME', 'njab'),
                        email=os.getenv('DJANGO_SUPERUSER_EMAIL', 'justenganongo@gmail.com'),
                        password=os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Mathjust')
                    )
                    print("✅ Superutilisateur créé automatiquement.")
                else:
                    print("ℹ️ Superutilisateur déjà existant.")
            except OperationalError:
                print("⚠️ Base de données non prête pour la création du superutilisateur.")
