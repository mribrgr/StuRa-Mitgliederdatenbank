from django.db import models

class Referat(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.bezeichnung
    def __unicode__(self):
        return u'%s' % self.bezeichnung

class Unterbereich(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    referat = models.ForeignKey(Referat, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.bezeichnung + " (Referat " + self.referat.__str__() + ")"
    def __unicode__(self):
        return u'%s' % self.bezeichnung

class Amt(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)
    workload = models.IntegerField(null=True)
    referat = models.ForeignKey(Referat, on_delete=models.CASCADE, null=False)
    unterbereich = models.ForeignKey(Unterbereich, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.bezeichnung + " " + self.referat.__str__()

class Recht(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)

class AmtRecht(models.Model):
    amt = models.ForeignKey(Amt, on_delete=models.CASCADE, null=False)
    recht = models.ForeignKey(Recht, on_delete=models.CASCADE, null=False)
