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
    path('contact_envoie/', views.contact_envoie, name='contact_envoie'),
    path('forum/', views.forum_index, name='forum_index'),
    path('forum/<int:categorie_id>/', views.forum_category, name='forum_category'),
    path('forum/<int:categorie_id>/topic/<int:topic_id>/', views.forum_topic, name='forum_topic'),
    path('forum/post/<int:post_id>/like/', views.forum_post_like, name='forum_post_like'),
    path('forum/post/<int:post_id>/report/', views.forum_post_report, name='forum_post_report'),
]
