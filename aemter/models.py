from django.db import models

class Referat(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)

class Unterbereich(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)

class Amt(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    workload = models.IntegerField(null=True)
    referat = models.ForeignKey(Referat, on_delete=models.CASCADE, null=False)
    unterbereich = models.ForeignKey(Unterbereich, on_delete=models.CASCADE, null=True)

class Recht(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)

class AmtRecht(models.Model):
    amt = models.ForeignKey(Amt, on_delete=models.CASCADE, null=False)
    recht = models.ForeignKey(Recht, on_delete=models.CASCADE, null=False)
