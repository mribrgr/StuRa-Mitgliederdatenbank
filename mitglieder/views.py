from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Mitglied, MitgliedAmt, MitgliedMail
from aemter.models import Amt, Referat, Unterbereich
import simplejson, json
from django.template import RequestContext

class CMitglied:
    def __init__(self):
        # super().__init__()
        self.mitid = ""
        self.amt = ""
        self.funktion = ""
        self.nachname = ""
        self.vorname = ""
        self.strasse = ""
        self.hausnr = ""
        self.plz = ""
        self.ort = ""
        self.telfestnetz = ""
        self.telmobil = ""
        self.email = ""
        self.jabberid = ""


aemternum = 0
emailnum = 0

"""
# Create your views here.
def main_screen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    my_list = []
    m = Mitglied()

    m.mitid = 100
    m.aemter = ["Wichtig", "Unwichtig"]
    m.funktion = "Tester"
    m.nachname = "Hirsch"
    m.vorname = "Lukas"
    m.strasse = "Straße der Jugend"
    m.hausnr = 21
    m.plz = "01561"
    m.ort = "Ebersbach"
    m.telfestnetz = "0352084822"
    m.telmobil = "01515444444"
    m.email = "s79199@htw-dresden.com"
    m.jabberid = 111
    my_list.append(m)

    m2 = Mitglied()
    m2.mitid = 101
    m2.aemter = ["Wichtig"]
    m2.funktion = "Tester"
    m2.nachname = "Hirsch"
    m2.vorname = "Florian"
    m2.strasse = "Straße der Jugend"
    m2.hausnr = 18
    m2.plz = "01561"
    m2.ort = "Ebersbach"
    m2.telfestnetz = "0352084822"
    m2.telmobil = "01515555555"
    m2.email = "sxxxxx@htw-dresden.com"
    m2.jabberid = 112
    my_list.append(m2)

    m3 = Mitglied()
    m3.mitid = 102
    m3.aemter = ["Wichtig"]
    m3.funktion = "Tester"
    m3.nachname = "Mustermann"
    m3.vorname = "Max"
    m3.strasse = "Musterstraße"
    m3.hausnr = 1349
    m3.plz = "01561"
    m3.ort = "Musterstadt"
    m3.telfestnetz = "0000000000"
    m3.telmobil = "0151000000"
    m3.email = "s00000@htw-dresden.com"
    m3.jabberid = 113
    my_list.append(m3)

    m4 = Mitglied()
    m4.mitid = 103
    m4.aemter = ["Wichtig"]
    m4.funktion = "Tester"
    m4.nachname = "Musterfrau"
    m4.vorname = "Maxi"
    m4.strasse = "Musterstraße"
    m4.hausnr = 184
    m4.plz = "01561"
    m4.ort = "Musterstadt"
    m4.telfestnetz = "111111111"
    m4.telmobil = "0151111111"
    m4.email = "s11111@htw-dresden.com"
    m4.jabberid = 114
    my_list.append(m4)
"""

def main_screen(request):
    # Create your views here.
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    my_list = Mitglied.objects.order_by('name')
    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})


def mitglieder_loeschen(request):
    mitgliederids = request.POST.get('mitglieder')
    mitgliederids = json.loads(mitgliederids)
    for mitgliedid in mitgliederids:
        Mitglied.objects.get(pk=mitgliedid).delete()
    return HttpResponse()

def mitgliedErstellenView(request):
  if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")
    global aemternum, emailnum
    aemternum = emailnum = 1
    referate = Referat.objects.order_by('bezeichnung')
"""
def mitglied_erstellen(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")

    context = {
        'referate_set': [
            {'name': 'Qualitaetsmanagement'},
            {'name': 'Kultur'},
            {'name': 'Finanzen'}
        ],
        'bereiche_set': [
            {'name': 'Keiner'},
            {'name': 'Bereich 1'},
            {'name': 'Bereich 2'}
        ],
        'aemter_set': [
            {'name': 'Leitung'},
            {'name': 'Stellvertretung'}
        ],
    }
"""
    return render(request=request,
                template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                context={'referate':referate, 'amtid': aemternum, 'emailid': emailnum})

def bereiche_laden(request):
    global aemternum
    referat_id = request.GET.get('referat')
    amtnum = request.GET.get('amtnum')
    bereiche = Referat.objects.get(pk=referat_id).unterbereich_set.all()
    return render(request, 'mitglieder/bereich_dropdown_list_options.html', {'bereiche': bereiche, 'amtid': amtnum})

def aemter_laden(request):
    global aemternum
    bereich_id = request.GET.get('bereich')
    amtnum = request.GET.get('amtnum')
    if bereich_id == "-1":
        referat_id = request.GET.get('referat')
        aemter = Referat.objects.get(pk=referat_id).amt_set.all()
        aemter = aemter.filter(unterbereich__isnull=True)
    else:
        aemter = Unterbereich.objects.get(pk=bereich_id).amt_set.all()
    return render(request, 'mitglieder/amt_dropdown_list_options.html', {'aemter': aemter, 'amtid': amtnum})

def aemter_html_laden(request):
    global aemternum
    aemternum += 1
    referate = Referat.objects.order_by('bezeichnung')
    return render(request, 'mitglieder/aemter.html', {'referate': referate, 'amtid': aemternum})

def amt_loeschen(request):
    global aemternum
    aemternum-=1
    return HttpResponse()

def email_html_laden(request):
    global emailnum
    emailnum +=1
    return render(request, 'mitglieder/email.html', {'emailid': emailnum})

def email_loeschen(request):
    global emailnum
    emailnum-=1
    return HttpResponse()

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

def mitgliedBearbeitenView(request):
#def mitglied_bearbeiten(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")

    if not request.user.is_superuser:
        messages.error(request, "Du musst Admin sein, um diese Seite aufrufen zu können.")
        return redirect("/mitglieder")

    m5 = Mitglied()
    m5.mitid = 104
    m5.aemter = [
        {
            'referat': 'Kultur',
            'bereich': None,
            'funktion': 'Referatsleitung',
            'beginn': '01.01.2020',
            'ende': '02.01.2020'
        },
        {
            'referat': 'Finanzen',
            'bereich': 'Haushalt',
            'funktion': 'Stellvertretende Bereichsleitung',
            'beginn': '06.06.2006'
        }
    ]

    m5.nachname = "Müller"
    m5.vorname = "Tobias"
    m5.strasse = "Feldweg"
    m5.hausnr = "666"
    m5.plz = "01111"
    m5.ort = "Dresden"
    m5.telfestnetz = "0348484857"
    m5.telmobil = "01515151515"
    m5.emails = [
        "Tobias.Müller@htw-dresden.com",
        's79188@htw-dresden.de'
    ]
    m5.jabberid = 115

    context = {
        'referate_set': [
            {'name': 'Qualitaetsmanagement'},
            {'name': 'Kultur'},
            {'name': 'Finanzen'}
        ],
        'bereiche_set': [
            {'name': 'Keiner'},
            {'name': 'Haushalt'},
            {'name': 'Anderer Bereich'}
        ],
        'aemter_set': [
            {'name': 'Leitung'},
            {'name': 'Stellvertretung'}
        ],
        'mitglied': m5
    }
    return render(request=request,
                  template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                  context = context)
