from django.db import models

class Referat(models.Model):
    bezeichnung = models.CharField(max_length=50)

class Unterbereich(models.Model):
    bezeichnung = models.CharField(max_length=50)

class Amt(models.Model):
    bezeichnung = models.CharField(max_length=50)
    workload = models.IntegerField()
    referat = models.ForeignKey(Referat)
    unterbereich = models.ForeignKey(Unterbereich)

class Recht(models.Model):
    bezeichnung = models.CharField(max_length=50)

class AmtRecht(models.Model):
    amt = models.ForeignKey(Amt)
    recht = models.ForeignKey(Recht)
