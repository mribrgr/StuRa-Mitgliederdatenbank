from django.shortcuts import render
from django.http import HttpResponse

class Mitglied:
    def __init__(self):
        # super().__init__()
        self.vorname = ""
        self.nickname = ""
        self.amt = ""
        self.funktion = ""
        self.email = ""
        self.telefonnummer = ""
        self.website = ""


# Create your views here.
def main_screen(request):

    my_list = []
    m = Mitglied()

    m.vorname = "Lukas Hirsch"
    m.nickname = "derhirsch"
    m.amt = "STURA"
    m.funktion = "Hausmeister"
    m.email = "sura@stura.de"
    m.telefonnummer = "+49 01521 484848"
    m.website = "www.kauft-mein-merch.org"
    my_list.append(m)

    m2 = Mitglied()
    m2.nickname = "derhirsch2"
    my_list.append(m2)

    m3 = Mitglied()
    m3.nickname = "derhirsch3"
    my_list.append(m3)

    m4 = Mitglied()
    m4.nickname = "derhirsch4"
    my_list.append(m4)

    m5 = Mitglied()
    m5.nickname = "derhirsch5"
    my_list.append(m5)
    
    return render(request=request,
                  template_name="mitglieder/mitglieder.html",
                  context = {"data":my_list})

#
# TODO: Richtige Probe Datensätze
# TODO: Preview Fesnster mit mehr inhalten
# 