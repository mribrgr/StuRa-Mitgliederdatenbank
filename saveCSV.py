import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bin.settings")
django.setup()


# your imports, e.g. Django models
from aemter.models import Referat, Amt, Unterbereich
import csv

Referat.objects.all().delete()
Unterbereich.objects.all().delete()
Amt.objects.all().delete()


with open("referate.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for referat in row:
            if not Referat.objects.filter(bezeichnung=referat).exists():
                r = Referat(bezeichnung=referat)
                r.save()
                print("Referat " + referat + " gespeichert")
                # Aemter
                a = Amt(bezeichnung="Leitung", referat=r)
                a.save()
                a = Amt(bezeichnung="Stellvertretende Leitung", referat=r)
                a.save()

            else:
                print("Referat " + referat + " existiert bereits")

with open("bereiche.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        referat = row.pop(0)
        print(referat)
        for bereich in row:
            if Unterbereich.objects.filter(bezeichnung=bereich).exists()==False:
                print("Bereich " + bereich + " (Referat: " + referat + ") wird gespeichert")
                b = Unterbereich(bezeichnung=bereich, referat=Referat.objects.get(bezeichnung=referat))
                b.save()
                # Aemter
                a = Amt(bezeichnung="Leitung", unterbereich=b, referat=b.referat)
                a.save()
                a = Amt(bezeichnung="Stellvertretende Leitung", unterbereich=b, referat=b.referat)
                a.save()
                a = Amt(bezeichnung="Beratendes Mitglied", unterbereich=b, referat=b.referat)
                a.save()
