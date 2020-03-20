from django.urls import path
from . import views


app_name = 'login'  # here for namespacing of urls.

urlpatterns = [
    path("", views.list, name="list"),
]