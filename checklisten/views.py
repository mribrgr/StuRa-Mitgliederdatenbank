from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Checkliste

def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    checklisten = Checkliste.objects.all()

    return render(request=request, 
                  template_name='checklisten/main_screen.html', 
                  context = {"checklisten": checklisten})

def erstellen(request):
    return redirect("/checklisten")

def abhaken(request):
    return redirect("/checklisten")
