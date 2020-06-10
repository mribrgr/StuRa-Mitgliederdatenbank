# -*- coding: utf-8 -*-

import os, django, sys
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bin.settings")
django.setup()

from aemter.models import Referat, Amt, Unterbereich
import csv

def importAemter(file):
    # Delete existing Data
    Referat.objects.all().delete()
    Unterbereich.objects.all().delete()
    Amt.objects.all().delete()

    # read CSV
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        referat = row[0]
        unterbereich = row[1]
        amt = row[2]

        # Print Current Line for Debug
        print(referat + " | " + unterbereich + " | " + amt)

        if (referat == 'Referat'):
            continue

        # Erstelle das Referat
        if not Referat.objects.filter(bezeichnung=referat).exists():
            new_referat = Referat(
                bezeichnung = referat
            )
            new_referat.save()
        else:
            new_referat = Referat.objects.get(bezeichnung=referat)

        # Erstelle den Unterbereich
        if not Unterbereich.objects.filter(bezeichnung=unterbereich).exists():
            new_unterbereich = None
            if (unterbereich != 'None'):
                new_unterbereich = Unterbereich(
                    bezeichnung = unterbereich,
                    referat = new_referat
                )
                new_unterbereich.save()
        else:
            new_unterbereich = Unterbereich.objects.get(bezeichnung=unterbereich)

        # Erstelle das Amt
        new_amt = Amt(
            bezeichnung = amt,
            workload = 5,
            referat = new_referat,
            unterbereich = new_unterbereich
        )
        new_amt.save()
    pass

if __name__ == "__main__":
    file = open("ReferateUnterbereicheAemter.csv", encoding="utf-8")
    importAemter(file)
