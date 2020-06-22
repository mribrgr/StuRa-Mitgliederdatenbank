from django.db import models
from simple_history.models import HistoricalRecords

from mitglieder.models import MitgliedAmt

class Checkliste(models.Model):
    mitgliedAmt = models.ForeignKey(MitgliedAmt, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()

class Aufgabe(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()

class ChecklisteAufgabe(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE, null=False)
    aufgabe = models.ForeignKey(Aufgabe, on_delete=models.CASCADE, null=False)
    abgehakt = models.BooleanField(default=False, null=False)
    history = HistoricalRecords()
