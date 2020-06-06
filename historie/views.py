from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator

from datetime import datetime

from mitglieder.models import Mitglied, MitgliedMail, MitgliedAmt
from aemter.models import Referat, Unterbereich, Amt, Recht, AmtRecht
from django.contrib.auth.models import User
from django.db.models import Q

def list(request):
    """
    Die einzige View der `historie`-App, welche das Anzeigen aller Historien-Einträge ermöglicht.

    Folgende Aufgaben werden durch diese übernommen:

    * Zugriffsbeschränkung: Zugriff wird nur gewährt, wenn der Nutzer angemeldet UND Administrator ist.
    * Bereitstellung der Daten: Die View holt sämtliche Historien-Einträge aus der Datenbank und stellt diese als Kontext bereit.
    * Rendern des Templates

    Je nachdem, ob in der `request` Suchbegriffe mitgegeben wurden, werden entweder alle Einträge oder die nach den Suchbegriffen
    gefilterten Einträge bereitgestellt. Die Filterung funktioniert dabei folgendermaßen:
    
    * Alle Models werden dahingehend untersucht, ob die wichtigsten Felder eines Eintrags (bei Mitgliedern z.B. ID, Vorname und Name) die Suchbegriffe enthalten.
    * Hierfür werden die in Django integrierten `Q Objects` verwendet.
    * Alle gefundenen Einträge werden in QuerySets zusammengefasst, welche anschließend an ``render`` übergeben werden.

    :param request: Die HTML-Request, welche den Aufruf der View ausgelöst hat. Enthält ggf. Suchbegriffe, nach welchen die Historien-Einträge gefiltert werden sollen.
    :return: Die gerenderte View.
    """
    # Access restrictions
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")

    # Fetch all entries
    mitglieder = Mitglied.history.all()
    mitgliederMails = MitgliedMail.history.all()
    mitgliederAemter = MitgliedAmt.history.all()

    referate = Referat.history.all()
    unterbereiche = Unterbereich.history.all()
    aemter = Amt.history.all()
    rechte = Recht.history.all()
    aemterRechte = AmtRecht.history.all()

    users = User.history.all()

    # Paginate results
    page_number = 1

    mitgliederPaginator = Paginator(mitglieder, 15)
    mitgliederMailsPaginator = Paginator(mitgliederMails, 15)
    mitgliederAemterPaginator = Paginator(mitgliederAemter, 15)
    referatePaginator = Paginator(referate, 15)
    unterbereichePaginator = Paginator(unterbereiche, 15)
    aemterPaginator = Paginator(aemter, 15)
    rechtePaginator = Paginator(rechte, 15)
    aemterRechtePaginator = Paginator(aemterRechte, 15)
    usersPaginator = Paginator(users, 15)

    mitgliederPage = mitgliederPaginator.get_page(page_number)
    mitgliederMailsPage = mitgliederMailsPaginator.get_page(page_number)
    mitgliederAemterPage = mitgliederAemterPaginator.get_page(page_number)
    referatePage = referatePaginator.get_page(page_number)
    unterbereichePage = unterbereichePaginator.get_page(page_number)
    aemterPage = aemterPaginator.get_page(page_number)
    rechtePage = rechtePaginator.get_page(page_number)
    aemterRechtePage = aemterRechtePaginator.get_page(page_number)
    usersPage = usersPaginator.get_page(page_number)

    return render(request=request,
                  template_name="historie/list.html",
                  context={"mitglieder": mitgliederPage,
                           "mitgliederMails": mitgliederMailsPage,
                           "mitgliederAemter": mitgliederAemterPage,
                           "referate": referatePage,
                           "unterbereiche": unterbereichePage,
                           "aemter": aemterPage,
                           "rechte": rechtePage,
                           "aemterRechte": aemterRechtePage,
                           "users": usersPage})

def fetch_entries(request):
    # Access restrictions
    if not request.user.is_authenticated:
        return HttpResponse("Permission denied")
    if not request.user.is_superuser:
        return HttpResponse("Permission denied")
    
    # Get data from request
    searchterm = request.GET.get('search')
    page_number = request.GET.get('page')
    selected_tab = request.GET.get('tab')
    
    # Get indvidiual search terms
    searchterms = None
    if searchterm:
        searchterms = searchterm.split(',')
        for term in searchterms:
            term = term.strip()
    
    if not searchterm:
        searchterms = [""]
    
    # Get data for selected tab and search terms
    data = None
    if selected_tab == "Mitglied":
        data = Mitglied.history.none()
        for term in searchterms:
            data = data | Mitglied.history.filter(Q(id__icontains=term) | Q(vorname__icontains=term) | Q(name__icontains=term))
    if selected_tab == "MitgliedMail":
        data = MitgliedMail.history.none()
        for term in searchterms:
            data =  data | MitgliedMail.history.filter(Q(mitglied__id__icontains=term) | Q(mitglied__vorname__icontains=term) | Q(mitglied__name__icontains=term) | Q(email__icontains=term))
    if selected_tab == "MitgliedAmt":
        data = MitgliedAmt.history.none()
        for term in searchterms:
             data = data | MitgliedAmt.history.filter(Q(mitglied__id__icontains=term) | Q(mitglied__vorname__icontains=term) | Q(mitglied__name__icontains=term) 
                | Q(amt__id__icontains=term) | Q(amt__bezeichnung__icontains=term) 
                | Q(amt__referat__bezeichnung__icontains=term)
                | Q(amt__unterbereich__bezeichnung__icontains=term))
    if selected_tab == "Referat":
        data = Referat.history.none()
        for term in searchterms:
            data = data | Referat.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term))
    if selected_tab == "Unterbereich":
        data = Unterbereich.history.none()
        for term in searchterms:
            data = data | Unterbereich.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term) | Q(referat__id__icontains=term) | Q(referat__bezeichnung__icontains=term))
    if selected_tab == "Amt":
        data = Amt.history.none()
        for term in searchterms:
            data = data | Amt.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term) 
                | Q(referat__id__icontains=term) | Q(referat__bezeichnung__icontains=term) 
                | Q(unterbereich__id__icontains=term) | Q(unterbereich__bezeichnung__icontains=term))
    if selected_tab == "Recht":
        data = Recht.history.none()
        for term in searchterms:
            data = data | Recht.history.filter(Q(id__icontains=term) | Q(bezeichnung__icontains=term))
    if selected_tab == "AmtRecht":
        data = AmtRecht.history.none()
        for term in searchterms:
            data = data | AmtRecht.history.filter(Q(amt__id__icontains=term) | Q(amt__bezeichnung__icontains=term) 
                | Q(amt__referat__bezeichnung__icontains=term)
                | Q(amt__unterbereich__bezeichnung__icontains=term)
                | Q(recht__id__icontains=term) |Q(recht__bezeichnung__icontains=term))
    if selected_tab == "User":
        data = User.history.none()
        for term in searchterms:
            data = data | User.history.filter(Q(username__icontains=term) | Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(email__icontains=term))

    # Paginate results
    paginator = Paginator(data, 15)
    data_page = paginator.get_page(page_number)

    return render(request=request,
                  template_name="historie/row.html",
                  context={"data": data_page})

