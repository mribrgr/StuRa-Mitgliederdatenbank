from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from simple_history.models import HistoricalRecords
from aemter.models import Funktion

class Mitglied(models.Model):
    name = models.CharField(max_length=50, null=False)
    vorname = models.CharField(max_length=50, null=False)
    spitzname = models.CharField(max_length=50, null=True)
    strasse = models.CharField(max_length=50, null=True)
    hausnr = models.CharField(null=True, max_length=10)
    plz = models.CharField(max_length=5, null=True)
    ort = models.CharField(max_length=50, null=True)
    tel_mobil = models.CharField(max_length=15, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.vorname + " " + self.name
    class Meta:
        verbose_name = "Mitglied"
        verbose_name_plural = "Mitglieder"


class MitgliedAmt(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    funktion = models.ForeignKey(Funktion, on_delete=models.CASCADE, null=False)
    amtszeit_beginn = models.DateField(null=True)
    amtszeit_ende = models.DateField(null=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.mitglied.__str__() + ", " + self.funktion.__str__()
    class Meta:
        verbose_name = "Zuordnung Mitglied-Amt"
        verbose_name_plural = "Zuordnungen Mitglied-Amt"

class MitgliedMail(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.email + " " + self.mitglied.__str__()
    class Meta:
        verbose_name = "Zuordnung Mitglied-Mail"
        verbose_name_plural = "Zuordnungen Mitglied-Mail"
