from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('galerie/', views.galerie, name='galerie'),
    path('commander/', views.commander, name='commander'),
    path('contact/', views.contact, name='contact'),
    path('oeuvre/<int:pk>/', views.oeuvre_detail, name='oeuvre_detail'),
    path('merci/', views.merci, name='merci'),
    path("create-superuser/", views.create_superuser_view),
]
