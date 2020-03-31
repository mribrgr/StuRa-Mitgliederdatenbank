from django.urls import path
from . import views


app_name = 'login'  # here for namespacing of urls.

urlpatterns = [
    path("", views.main_screen, name="homepage"),
    path("erstellen", views.mitglied_erstellen, name="erstellen"),
    path("bearbeiten", views.mitglied_bearbeiten, name="bearbeiten"),
]