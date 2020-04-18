from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Mitglied, MitgliedAmt, MitgliedMail
from aemter.models import Amt, Referat, Unterbereich
import simplejson, json
# string splitting
import re
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
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    my_list = Mitglied.objects.order_by('vorname', 'name')
    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})

def mitglied_laden(request):
    mitglied_id = simplejson.loads(request.GET.get('mitgliedid'))
    print(mitglied_id)
    mitglied = Mitglied.objects.get(pk=mitglied_id)
    return render(request, 'mitglieder/modal.html', {'mitglied': mitglied})

def mitglieder_loeschen(request):
    mitgliederids = request.POST.get('mitglieder')
    mitgliederids = json.loads(mitgliederids)
    print(mitgliederids)
    for mitgliedid in mitgliederids:
        Mitglied.objects.get(pk=mitgliedid).delete()

    return HttpResponse()

def mitgliedErstellenView(request):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
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

def mitgliedBearbeitenView(request, mitglied_id):
    if not request.user.is_authenticated:
        messages.error(request, "Du musst angemeldet sein, um diese Seite sehen zu können.")
        return redirect("/")
    global aemternum, emailnum
    
    mitglied = Mitglied.objects.get(pk=mitglied_id)
    aemternum = mitglied.mitgliedamt_set.all().count()
    emailnum = mitglied.mitgliedmail_set.all().count()
    referate = Referat.objects.order_by('bezeichnung')

    return render(request=request,
                  template_name="mitglieder/mitglied_erstellen_bearbeiten.html",
                  context = {'mitglied': mitglied, 'referate': referate})

def speichern(request):
    if request.method == 'POST':
        mitglied = Mitlied.objects.get(pk=9)
        # Mitglied
        vorname = request.POST['vorname']
        nachname = request.POST['nachname']
        spitzname = request.POST['spitzname']
        strasse = request.POST['strasse']
        hausnr = request.POST['hausnr']
        plz = request.POST['plz']
        ort = request.POST['ort']
        telefon_mobil = request.POST['telefon_mobil']

        mitglied.vorname = vorname
        mitglied.name = nachname
        mitglied.spitzname = spitzname
        mitglied.strasse = strasse
        mitglied.hausnr = hausnr
        mitglied.plz = plz
        mitglied.ort = ort
        mitglied.tel_mobil = telefon_mobil
        mitglied.save()

        newaemter = Amt.objects.none()
        for i in range(1, aemternum+1):
            amt_id = request.POST['selectamt'+str(i)]
            amt = Amt.objects.get(pk=amt_id)
            mitgliedamt = MitgliedAmt(amt=amt, mitglied=mitglied)
            mitgliedamt.save()

        newemails = MitgliedMail.objects.none()
        for i in range(1, emailnum+1):
            email = request.POST['email'+str(i)]
            mitgliedmail = MitgliedMail(email=email, mitglied=mitglied)
            mitgliedmail.save()
    return HttpResponseRedirect(reverse('mitglieder:homepage'))

def suchen(request, search_string):
    # split ", " or " "
    search_tokens = re.split(', | ', search_string)
    my_list = Mitglied.objects.none()
    for token in search_tokens:
        my_list = (my_list | Mitglied.objects.filter(name__icontains=token)).distinct()
        my_list = (my_list | Mitglied.objects.filter(vorname__icontains=token)).distinct()
    print(my_list)
    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})
