from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('galerie/', views.galerie, name='galerie'),
    path('commander/', views.commander, name='commander'),
    path('contact/', views.contact, name='contact'),
    path('oeuvre/<int:pk>/', views.detail_oeuvre, name='detail_oeuvre'),
    path('init-categories/', views.init_categories, name='init_categories'),
]
