from django.db import models

class Checkliste(models.Model):
    mitglied = models.ForeignKey(Mitglied)

class Aufgabe(models.Model):
    bezeichnung = models.CharField(max_length=50)

class ChecklisteAufgabe(models.Model):
    checkliste = models.ForeignKey(Checkliste)
    aufgabe = models.ForeignKey(Aufgabe)
    abgehakt = models.BooleanField(default=False)
