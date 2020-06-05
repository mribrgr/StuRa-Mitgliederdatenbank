from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator
from .models import Mitglied, MitgliedAmt, MitgliedMail
from aemter.models import Amt, Referat, Unterbereich
import simplejson, json
# string splitting
import re
from django.template import RequestContext
from django.db.models import Q

# Anzahl der Aemter bzw. E-Mails die gespeichert werden muessen
aemternum = 0
emailnum = 0

# Mitgliederanzeige
def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    # Paginate data
    queryset = Mitglied.objects.order_by('vorname', 'name')
    paginator = Paginator(queryset, 2) # Show 15 entries per page
    page_number = request.GET.get('page') # Get page number from request
    queryset_page = paginator.get_page(page_number) # Get entries for that page

    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":queryset_page, "search_string": None})

# Senden eines Mitglieds an das Frontend fuer das Modal
def mitglied_laden(request):
    # Extrahieren der Mitglied-Id aus der GET-Request
    mitglied_id = simplejson.loads(request.GET.get('mitgliedid'))
    # Daten zum Mitglied mit dieser Id an Frontend senden
    mitglied = Mitglied.objects.get(pk=mitglied_id)
    return render(request, 'mitglieder/modal.html', {'mitglied': mitglied})

# Entfernen von Mitgliedern aus der Datenbank
def mitglieder_loeschen(request):
    # Extrahieren der Liste aller Mitglied-Ids und Entfernen der Mitglieder aus Datenbank
    mitgliederids = request.POST.get('mitglieder')
    mitgliederids = json.loads(mitgliederids)
    for mitgliedid in mitgliederids:
        Mitglied.objects.get(pk=mitgliedid).delete()
    return HttpResponse()

# Mitglied erstellen Anzeige
def mitgliedErstellenView(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    # beim Erstellen existiert anfangs jeweils ein Feld fuer Amt und E-Mail
    global aemternum, emailnum
    aemternum = emailnum = 1
    # Laden aller Referate
    referate = Referat.objects.order_by('bezeichnung')
    # Anzahl von E-Mails, Aemtern sowie Referate werden an Frontend gesendet
    return render(request=request,
        template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
        context={'referate':referate, 'amtid': aemternum, 'emailid': emailnum})

# Unterbereiche eines Referats an das Frontend senden        
def bereiche_laden(request):
    global aemternum
    referat_id = request.GET.get('referat')
    amtnum = request.GET.get('amtnum')
    bereiche = Referat.objects.get(pk=referat_id).unterbereich_set.all()
    return render(request, 'mitglieder/bereich_dropdown_list_options.html', {'bereiche': bereiche, 'amtid': amtnum})

# Aemter eines Bereichs an das Frontend senden
def aemter_laden(request):
    global aemternum
    bereich_id = request.GET.get('bereich')
    amtnum = request.GET.get('amtnum')
    # als Bereich wurde "keiner" gewaehlt => nur Aemter des Referats ohne Bereich werden geladen
    if bereich_id == "-1":
        referat_id = request.GET.get('referat')
        aemter = Referat.objects.get(pk=referat_id).amt_set.all()
        aemter = aemter.filter(unterbereich__isnull=True)
    # Laden aller Aemter fuer gewaehlten Unterbereich
    else:
        aemter = Unterbereich.objects.get(pk=bereich_id).amt_set.all()
    return render(request, 'mitglieder/amt_dropdown_list_options.html', {'aemter': aemter, 'amtid': amtnum})

# Formular fuer ein Amt hinzufuegen (Mitglied erstellen/bearbeiten)
def aemter_html_laden(request):
    global aemternum
    aemternum += 1
    referate = Referat.objects.order_by('bezeichnung')
    # Senden von aemternum an Frontend, um HTML-Elementen richtige Id zuzuordnen
    return render(request, 'mitglieder/aemter.html', {'referate': referate, 'amtid': aemternum})

# Formular fur ein Amt loeschen (Mitglied erstellen/bearbeiten)
def amt_loeschen(request):
    global aemternum
    aemternum-=1
    return HttpResponse()

# Formular fur eine E-Mail hinzufuegen (Mitglied erstellen/bearbeiten)
def email_html_laden(request):
    global emailnum
    emailnum +=1
    return render(request, 'mitglieder/email.html', {'emailid': emailnum})

# Formular fur eine E-Mail loeschen (Mitglied erstellen/bearbeiten)
def email_loeschen(request):
    global emailnum
    emailnum-=1
    return HttpResponse()

# Mitglied erstellen
def erstellen(request):
    global aemternum, emailnum
    if request.method == 'POST':
        # Mitglied
        vorname = request.POST['vorname']
        nachname = request.POST['nachname']
        spitzname = request.POST['spitzname']
        strasse = request.POST['strasse']
        hausnr = request.POST['hausnr']
        plz = request.POST['plz']
        ort = request.POST['ort']
        telefon_mobil = request.POST['telefon_mobil']
        mitglied = Mitglied(name=nachname, vorname=vorname, spitzname=spitzname, strasse=strasse, hausnr=hausnr, plz=plz, ort=ort, tel_mobil=telefon_mobil)
        mitglied.save()

        for i in range(1, aemternum+1):
            amt_id = request.POST['selectamt'+str(i)]
            amt = Amt.objects.get(pk=amt_id)
            mitgliedamt = MitgliedAmt(amt=amt, mitglied=mitglied)
            mitgliedamt.save()
        for i in range(1, emailnum+1):
            email = request.POST['email'+str(i)]
            mitgliedmail = MitgliedMail(email=email, mitglied=mitglied)
            mitgliedmail.save()
        return HttpResponseRedirect(reverse('mitglieder:homepage'))
    else:
        return HttpResponseRedirect('/mitglieder/erstellen')

def mitgliedBearbeitenView(request, mitglied_id):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    global aemternum, emailnum
    
    mitglied = Mitglied.objects.get(pk=mitglied_id)
    aemternum = max(1, mitglied.mitgliedamt_set.all().count())
    emailnum = max(1, mitglied.mitgliedmail_set.all().count())
    referate = Referat.objects.order_by('bezeichnung')

    return render(request=request,
                  template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                  context = {'mitglied': mitglied, 'referate': referate})

# Attribut attr (string) wird aus request (POST-Request) entnommen und zurueckgegeben
# bei einem KeyError oder leerem String wird None zurueckgegeben
def getValue(request, attr):
    try:
        val = request.POST[attr]
        if val=="":
            val=None
    except KeyError:
        print("KeyError for attribute " + attr)
        val = None
    return val


# bearbeitetes Mitglied speichern
def speichern(request, mitglied_id):
    print("speichern")
    if request.method == 'POST':
        mitglied = Mitglied.objects.get(id=mitglied_id)
        # Mitglied
        mitglied.vorname = getValue(request, 'vorname')
        mitglied.name = getValue(request, 'nachname')
        mitglied.spitzname = getValue(request, 'spitzname')
        mitglied.strasse = getValue(request, 'strasse')
        mitglied.hausnr = getValue(request, 'hausnr')
        mitglied.plz = getValue(request, 'plz')
        mitglied.ort = getValue(request, 'ort')
        mitglied.tel_mobil = getValue(request, 'telefon_mobil')
        mitglied.save()

        mitglied.mitgliedamt_set.all().delete()
        for i in range(1, aemternum+1):
            amt_id = request.POST['selectamt'+str(i)]
            amt = Amt.objects.get(pk=amt_id)
            mitgliedamt = MitgliedAmt(amt=amt, mitglied=mitglied)
            mitgliedamt.save()

        mitglied.mitgliedmail_set.all().delete()
        for i in range(1, emailnum+1):
            email = request.POST['email'+str(i)]
            mitgliedmail = MitgliedMail(email=email, mitglied=mitglied)
            mitgliedmail.save()
    return HttpResponseRedirect(reverse('mitglieder:homepage'))

# Suche in der Mitgliederanzeige
def suchen(request):
    # Get parameters from request
    search_string = request.GET.get('search_string')
    page_number = request.GET.get('page')

    # Trennzeichen: ", ", "," oder " "
    tokens = re.split(', |,| ', search_string)
    # leere Strings aus Liste entfernen
    search_tokens = [t for t in tokens if t]

    if not search_tokens:
        # Paginate data
        queryset = Mitglied.objects.order_by('vorname', 'name')
        paginator = Paginator(queryset, 2) # Show 15 entries per page
        queryset_page = paginator.get_page(page_number) # Get entries for that page

        return render(request=request,
                  template_name="mitglieder/row.html",
                  context = {"data": queryset_page, "search_string": None})

    # Hinzufuegen aller Mitglieder zum QuerySet, deren Vor- oder Nachnamen ein Token enthalten
    matches={}
    for token in search_tokens:
        mitglieder_name_matches = Mitglied.objects.filter(name__icontains=token)
        mitglieder_vorname_matches = Mitglied.objects.filter(vorname__icontains=token)
        # Speichern, wie viele Matches es fuer jedes Mitglied gibt
        for queryset in mitglieder_name_matches, mitglieder_vorname_matches:
            for m in queryset:
                if m.id in matches:
                    matches[m.id]+=1
                else:
                    matches[m.id]=1
    
    # Mitglieder-Ids nach Anzahl der Matches sortieren
    matches_sorted = {k: v for k, v in sorted(matches.items(), key=lambda item: item[1])}
    # Mitgliederliste fuellen
    mitglieder_matches = []
    mitglied = lambda pk : Mitglied.objects.get(id=pk)
    for mitid in matches_sorted :
        print(str(mitid) + " " + str(matches[mitid]))
        print(mitglied(mitid))
        mitglieder_matches.insert(0, mitglied(mitid))

    # Paginate data
    paginator = Paginator(mitglieder_matches, 2) # Show 15 entries per page
    mitglieder_matches_page = paginator.get_page(page_number) # Get entries for that page

    return render(request=request,
                  template_name="mitglieder/row.html",
                  context = {"data": mitglieder_matches_page, "search_string": search_string})
