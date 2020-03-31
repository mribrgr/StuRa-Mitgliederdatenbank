from django.db import models

class Mitglied(models.Model):
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=50)
    plz = models.CharField(max_length=5)
    ort = models.CharField(max_length=50)
    tel_festnetz = models.CharField(max_length=15)
    tel_mobil = models.CharField(max_length=15)
    mail_privat = models.CharField(max_length=50)
    jabber_id = models.CharField(max_length=50)
