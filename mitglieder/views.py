from django.shortcuts import render, get_object_or_404
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

def main_screen(request):

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
    global aemternum, emailnum
    aemternum = emailnum = 1
    referate = Referat.objects.order_by('bezeichnung')
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
