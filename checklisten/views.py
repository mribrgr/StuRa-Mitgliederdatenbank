from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Checkliste, ChecklisteAufgabe, ChecklisteRecht, Aufgabe
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
    if not request.user.is_authenticated:
        return HttpResponse("Permission denied")
    if not request.user.is_superuser:
        return HttpResponse("Permission denied")

    # Get data from request
    mitglied_id = request.POST.get("mitgliedSelect")
    funktion_id = request.POST.get("funktionSelect")
    includeGeneralTasks = request.POST.get("generalTasksCheckbox")

    # Determine if general tasks shall be included
    if includeGeneralTasks == "on" or includeGeneralTasks is None and funktion_id == "-1":
        includeGeneralTasks = True
    else:
        includeGeneralTasks = False

    # Get foreign data
    mitglied = Mitglied.objects.get(id=mitglied_id)
    if not mitglied:
        return HttpResponse("Mitglied does not exist")
    
    # Get funktion if selected
    funktion = None
    if funktion_id != "-1":
        funktion = MitgliedAmt.objects.get(id=funktion_id)
        if not funktion:
            return HttpResponse("Funktion does not exist")

    existing = Checkliste.objects.filter(mitglied=mitglied, amt=funktion)
    if existing:
        messages.error(request, "Es existiert bereits eine Checkliste für dieses Mitglied und diese Funktion.")
        return redirect("/checklisten")

    # Create checkliste
    checkliste = Checkliste(mitglied=mitglied, amt=funktion)
    checkliste.save()

    # Add general tasks if selected
    if includeGeneralTasks == True:
        for task in Aufgabe.objects.all():
            aufgabe = ChecklisteAufgabe(checkliste=checkliste, aufgabe=task)
            aufgabe.save()
    
    # Add Rechte if Funktion was selected
    if funktion is not None:
        for funktion_recht in FunktionRecht.objects.filter(funktion__id=funktion.funktion.id):
            perm = funktion_recht.recht
            recht = ChecklisteRecht(checkliste=checkliste, recht=perm)
            recht.save()

    return redirect("/checklisten")

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