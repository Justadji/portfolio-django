from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galerie/', views.galerie, name='galerie'),
    path('commander/', views.commander, name='commander'),
    path('contact/', views.contact, name='contact'),
    path('oeuvre/<int:pk>/', views.detail_oeuvre, name='detail_oeuvre'),
]


