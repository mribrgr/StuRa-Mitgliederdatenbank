# -*- coding: utf-8 -*-

import os, django, sys
sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bin.settings")
django.setup()

from aemter.models import Organisationseinheit, Funktion, Unterbereich
import csv

def importAemter(file):
    # Delete existing Data
    Organisationseinheit.objects.all().delete()
    Unterbereich.objects.all().delete()
    Funktion.objects.all().delete()

    # read CSV
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        referat = row[0]
        unterbereich = row[1]
        funktion = row[2]

        # Print Current Line for Debug
        # print(referat + " | " + unterbereich + " | " + funktion)

        if (referat == 'Organisationseinheit'):
            continue

        # Erstelle das Organisationseinheit
        if not Organisationseinheit.objects.filter(bezeichnung=referat).exists():
            new_referat = Organisationseinheit(
                bezeichnung = referat
            )
            new_referat.save()
        else:
            new_referat = Organisationseinheit.objects.get(bezeichnung=referat)

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

        # Erstelle das Funktion
        new_amt = Funktion(
            bezeichnung = funktion,
            workload = 5,
            referat = new_referat,
            unterbereich = new_unterbereich
        )
        new_amt.save()
    pass

if __name__ == "__main__":
    file = open("ReferateUnterbereicheAemter.csv", encoding="utf-8")
    importAemter(file)
