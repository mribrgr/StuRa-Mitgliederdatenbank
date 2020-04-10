from django.urls import path
from . import views


app_name = 'mitglieder'  # here for namespacing of urls.

urlpatterns = [
    path("", views.main_screen, name="homepage"),
    path("erstellen", views.mitgliedErstellenView, name="erstellenView"),
    path("bearbeiten", views.mitgliedBearbeitenView, name="bearbeitenView"),
    path("erstellen/speichern", views.erstellen, name="erstellen"),

# Mitglieder Erstellen View
    path('ajax/bereiche-laden', views.bereiche_laden, name='bereiche_laden'),
    path('ajax/aemter-laden', views.aemter_laden, name='aemter_laden'),
    path('ajax/aemter-html-laden', views.aemter_html_laden, name='aemter_html_laden')

]
