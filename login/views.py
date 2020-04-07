from django.shortcuts import render, redirect

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def main_screen(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Herzlich Willkommen, {username}!")
                return redirect('/mitglieder')
            else:
                messages.error(request, "Benutzername oder Passwort ungültig.")
        else:
            messages.error(request, "Benutzername oder Passwort ungültig.")

    form = AuthenticationForm()

    return render(request=request,
                  template_name="login/login.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Bis zum nächsten Mal!")
    return redirect("/")
