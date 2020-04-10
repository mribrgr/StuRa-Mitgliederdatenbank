from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Mitglied, MitgliedAmt
from aemter.models import Amt, Referat, Unterbereich
import simplejson

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

# Create your views here.
def main_screen(request):

    my_list = Mitglied.objects.order_by('name')
    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})

def mitgliedErstellenView(request):
    global aemternum
    aemternum = 1
    referate = Referat.objects.order_by('bezeichnung')
    return render(request=request,
                template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                context={'referate':referate, 'amtid': aemternum})

def bereiche_laden(request):
    referat_bez = request.GET.get('referat')
    bereiche = Referat.objects.get(bezeichnung=referat_bez).unterbereich_set.all()
    return render(request, 'mitglieder/bereich_dropdown_list_options.html', {'bereiche': bereiche})

def aemter_laden(request):
    bereich_bez = request.GET.get('bereich')
    print(type(bereich_bez))
    if bereich_bez == "Keiner":
        referat_bez = request.GET.get('referat')
        aemter = Referat.objects.get(bezeichnung=referat_bez).amt_set.all()
        aemter = aemter.filter(unterbereich__isnull=True)
    else:
        print("Bereich: " + bereich_bez)
        aemter = Unterbereich.objects.get(bezeichnung=bereich_bez).amt_set.all()
    return render(request, 'mitglieder/amt_dropdown_list_options.html', {'aemter': aemter})

def aemter_html_laden(request):
    global aemternum
    aemternum += 1
    referate = Referat.objects.order_by('bezeichnung')
    return render(request, 'mitglieder/aemter.html', {'referate': referate, 'amtid': aemternum})

def erstellen(request):
    print("Mitglied wurde erstellt")
    return HttpResponseRedirect(reverse('mitglieder:homepage'))

def mitgliedBearbeitenView(request):
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
