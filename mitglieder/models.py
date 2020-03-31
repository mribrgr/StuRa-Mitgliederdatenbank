from django.db import models

from aemter.models import Amt

class Mitglied(models.Model):
    name = models.CharField(max_length=50, null=False)
    vorname = models.CharField(max_length=50, null=False)
    strasse = models.CharField(max_length=50, null=True)
    hausnr = models.IntegerField(null=True)
    plz = models.CharField(max_length=5, null=True)
    ort = models.CharField(max_length=50, null=True)
    tel_festnetz = models.CharField(max_length=15, null=True)
    tel_mobil = models.CharField(max_length=15, null=True)
    mail_privat = models.CharField(max_length=50, null=True)
    jabber_id = models.CharField(max_length=50, null=True)

class MitgliedAmt(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    amt = models.ForeignKey(Amt, on_delete=models.CASCADE, null=False)
