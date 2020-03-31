from django.shortcuts import render
from django.http import HttpResponse

class Mitglied:
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

    my_list = []
    m = Mitglied()

    m.mitid = 100
    m.amt = "Wichtig"
    m.funktion = "Tester"
    m.nachname = "Hirsch"
    m.vorname = "Lukas"
    m.strasse = "Straße der Jugend"
    m.plz = "01561"
    m.ort = "Ebersbach"
    m.telfestnetz = "0352084822"
    m.telmobil = "01515444444"
    m.email = "s79199@htw-dresden.com"
    m.jabberid = 111
    my_list.append(m)

    m2 = Mitglied()
    m2.mitid = 101
    m2.amt = "Wichtig"
    m2.funktion = "Tester"
    m2.nachname = "Hirsch"
    m2.vorname = "Florian"
    m2.strasse = "Straße der Jugend"
    m2.plz = "01561"
    m2.ort = "Ebersbach"
    m2.telfestnetz = "0352084822"
    m2.telmobil = "01515555555"
    m2.email = "sxxxxx@htw-dresden.com"
    m2.jabberid = 112
    my_list.append(m2)

    m3 = Mitglied()
    m3.mitid = 102
    m3.amt = "Wichtig"
    m3.funktion = "Tester"
    m3.nachname = "Mustermann"
    m3.vorname = "Max"
    m3.strasse = "Musterstraße"
    m3.plz = "01561"
    m3.ort = "Musterstadt"
    m3.telfestnetz = "0000000000"
    m3.telmobil = "0151000000"
    m3.email = "s00000@htw-dresden.com"
    m3.jabberid = 113
    my_list.append(m3)

    m4 = Mitglied()
    m4.mitid = 103
    m4.amt = "Wichtig"
    m4.funktion = "Tester"
    m4.nachname = "Musterfrau"
    m4.vorname = "Maxi"
    m4.strasse = "Musterstraße"
    m4.plz = "01561"
    m4.ort = "Musterstadt"
    m4.telfestnetz = "111111111"
    m4.telmobil = "0151111111"
    m4.email = "s11111@htw-dresden.com"
    m4.jabberid = 114
    my_list.append(m4)

    m5 = Mitglied()
    m5.mitid = 104
    m5.amt = "Wichtig"
    m5.funktion = "Tester"
    m5.nachname = "Müller"
    m5.vorname = "Tobias"
    m5.strasse = "Feldweg"
    m5.plz = "01111"
    m5.ort = "Dresden"
    m5.telfestnetz = "0348484857"
    m5.telmobil = "01515151515"
    m5.email = "Tobias.Müller@htw-dresden.com"
    m5.jabberid = 115
    my_list.append(m5)
    
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
            {'name': 'Bereich 1'},
            {'name': 'Bereich 2'}
        ]
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
            'funktion': 'Referatsleitung'
        },
        {
            'referat': 'Finanzen',
            'bereich': 'Haushalt',
            'funktion': 'Stellvertretende Bereichsleitung'
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
    m5.email = "Tobias.Müller@htw-dresden.com"
    m5.jabberid = 115

    context = {
        'referate_set': [
            {'name': 'Qualitaetsmanagement'},
            {'name': 'Kultur'},
            {'name': 'Finanzen'}
        ],
        'bereiche_set': [
            {'name': 'Haushalt'},
            {'name': 'Anderer Bereich'}
        ],
        'mitglied': m5
    }
    return render(request=request,
                  template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                  context = context)
