from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Mitglied, MitgliedAmt

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


# Create your views here.
def main_screen(request):

    my_list = Mitglied.objects.order_by('name')
    for mitglied in my_list:
        print(mitglied.tel_mobil)
        print(mitglied.vorname)

    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})

def mitglied_erstellen(request):
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
    return render(request=request,
                  template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                  context=context)

def mitglied_bearbeiten(request):
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
