from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Checkliste, ChecklisteAufgabe, ChecklisteRecht
from aemter.models import FunktionRecht
from mitglieder.models import Mitglied, MitgliedAmt

def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    checklisten = Checkliste.objects.all()
    mitglieder = Mitglied.objects.all().order_by('-id')[:20]

    return render(request=request, 
                  template_name='checklisten/main_screen.html', 
                  context = {"checklisten": checklisten, "mitglieder": mitglieder})

def erstellen(request):
    return HttpResponse()

def abhaken(request):
    if not request.user.is_authenticated:
        return HttpResponse("Nice try, FBI.")
    if not request.user.is_superuser:
        return HttpResponse("No way, CIA.")

    task_type = request.POST.get('task_type')
    if(task_type != "Aufgabe" and task_type != "Recht"):
        return HttpResponse("Invalid task_type")

    task_id = request.POST.get('task_id')
    if not task_id:
        return HttpResponse("No task_id provided")

    task = None
    if task_type == "Aufgabe":
        task = ChecklisteAufgabe.objects.get(id=task_id)
    if task_type == "Recht":
        task = ChecklisteRecht.objects.get(id=task_id)
    if not task:
        return HttpResponse("Invalid task_id")

    task.abgehakt = not task.abgehakt
    task.save()

    return HttpResponse()

def loeschen(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not today, NSA.")
    if not request.user.is_superuser:
        return HttpResponse("Good trick, MI6.")

    checkliste_id = request.POST.get('checkliste_id')
    if not checkliste_id:
        return HttpResponse("No checkliste_id provided")
    checkliste = Checkliste.objects.get(id=checkliste_id)
    if not checkliste:
        return HttpResponse("Invalid checkliste_id")

    checkliste.delete()

    return HttpResponse()

def get_funktionen(request):
    if not request.user.is_authenticated:
        return HttpResponse("Permission denied")
    if not request.user.is_superuser:
        return HttpResponse("Permission denied")

    mitglied_id = request.GET.get('mitglied_id')
    if not mitglied_id:
        return HttpResponse("No mitglied_id provided")
    funktionen = MitgliedAmt.objects.filter(mitglied__id=mitglied_id)

    return render(request=request, 
                  template_name='checklisten/_funktionSelectOptions.html', 
                  context = {"funktionen": funktionen})