from django.db import models
from simple_history.models import HistoricalRecords

from mitglieder.models import MitgliedAmt

class Checkliste(models.Model):
    mitgliedAmt = models.ForeignKey(MitgliedAmt, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Checkliste"
        verbose_name_plural = "Checklisten"

class Aufgabe(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Aufgabe"
        verbose_name_plural = "Aufgaben"

class ChecklisteAufgabe(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE, null=False)
    aufgabe = models.ForeignKey(Aufgabe, on_delete=models.CASCADE, null=False)
    abgehakt = models.BooleanField(default=False, null=False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Zuordnung Checkliste-Aufgabe"
        verbose_name_plural = "Zuordnungen Checkliste-Aufgabe"
