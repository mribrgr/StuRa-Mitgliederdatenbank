from django.db import models

from aemter.models import Amt

class Mitglied(models.Model):
    name = models.CharField(max_length=50, null=False)
    vorname = models.CharField(max_length=50, null=False)
    spitzname = models.CharField(max_length=50, null=True)
    strasse = models.CharField(max_length=50, null=True)
    hausnr = models.IntegerField(null=True)
    plz = models.CharField(max_length=5, null=True)
    ort = models.CharField(max_length=50, null=True)
    tel_mobil = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.vorname + " " + self.name

class MitgliedAmt(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    amt = models.ForeignKey(Amt, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.mitglied.__str__() + ", " + self.amt.__str__()

class MitgliedMail(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.email + " " + self.mitglied.__str__()
