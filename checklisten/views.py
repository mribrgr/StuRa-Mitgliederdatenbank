from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Checkliste, ChecklisteAufgabe, ChecklisteRecht
from aemter.models import FunktionRecht

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
    if not request.user.is_authenticated:
        return HttpResponse("Permission denied")
    if not request.user.is_superuser:
        return HttpResponse("Permission denied")

    task_type = request.POST.get('task_type')
    if(task_type != "Aufgabe" and task_type != "Recht"):
        return HttpResponse("Invalid task_type")

    task_id = request.POST.get('task_id')

    task = None
    if task_type == "Aufgabe":
        task = ChecklisteAufgabe.objects.get(id=task_id)
    if task_type == "Recht":
        task = ChecklisteRecht.objects.get(id=task_id)
    if not task:
        return HttpResponse("Invalid task_id")

    task.abgehakt = not task.abgehakt
    task.save()

    return redirect("/checklisten")

def loeschen(request):
    return redirect("/checklisten")
