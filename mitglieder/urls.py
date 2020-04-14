from django.urls import path
from . import views

#app_name = 'mitglieder'  # here for namespacing of urls.

urlpatterns = [
    path("", views.main_screen, name="main"),
    path("erstellen", views.mitgliedErstellenView, name="erstellenView"),
    path("bearbeiten", views.mitgliedBearbeitenView, name="bearbeitenView"),
    path("ajax/mitglieder-loeschen", views.mitglieder_loeschen, name="mitglieder_loeschen"),

# Mitglieder Erstellen View    
    path("erstellen/speichern", views.erstellen, name="erstellen"),
    path('ajax/bereiche-laden', views.bereiche_laden, name='bereiche_laden'),
    path('ajax/aemter-laden', views.aemter_laden, name='aemter_laden'),
    path('ajax/aemter-html-laden', views.aemter_html_laden, name='aemter_html_laden'),
    path('ajax/email-html-laden', views.email_html_laden, name='email_html_laden'),
    path('ajax/amt-loeschen', views.amt_loeschen, name='amt_loeschen'),
    path('ajax/email-loeschen', views.email_loeschen, name='email_loeschen'),
]
