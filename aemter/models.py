from django.db import models
from simple_history.models import HistoricalRecords

class Organisationseinheit(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.bezeichnung
    def __unicode__(self):
        return u'%s' % self.bezeichnung

class Unterbereich(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    organisationseinheit = models.ForeignKey(Organisationseinheit, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.bezeichnung + " (Organisationseinheit " + self.organisationseinheit.__str__() + ")"
    def __unicode__(self):
        return u'%s' % self.bezeichnung

class Funktion(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    workload = models.IntegerField(null=True)
    organisationseinheit = models.ForeignKey(Organisationseinheit, on_delete=models.CASCADE, null=False)
    unterbereich = models.ForeignKey(Unterbereich, on_delete=models.CASCADE, null=True)
    history = HistoricalRecords()
    def __str__(self):
        if self.unterbereich is None:
            return self.bezeichnung + " " + self.organisationseinheit.__str__()
        else:
            return self.bezeichnung + ' ' + self.unterbereich.__str__()

class Recht(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()

class FunktionRecht(models.Model):
    funktion = models.ForeignKey(Funktion, on_delete=models.CASCADE, null=False)
    recht = models.ForeignKey(Recht, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()
