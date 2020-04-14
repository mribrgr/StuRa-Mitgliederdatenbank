from django.urls import path
from . import views


#app_name = 'mitglieder'  # here for namespacing of urls.

urlpatterns = [
    path("", views.main_screen, name="main"),
    path("erstellen", views.mitglied_erstellen, name="erstellen"),
    path("bearbeiten", views.mitglied_bearbeiten, name="bearbeiten"),
]