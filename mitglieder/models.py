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


class MitgliedAmt(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    funktion = models.ForeignKey(Funktion, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.mitglied.__str__() + ", " + self.funktion.__str__()

@receiver(post_delete, sender=MitgliedAmt)
def delete_MitgliedAmt_hook(sender, instance, using, **kwargs):
    # print("post_delete")
    # Überprüfen ob schon eine PrevMitgliedAmt Liste für die funktion da ist
    if PrevMitgliedAmt.objects.filter(funktion=instance.funktion).count() != 0:
        # es ist schon eins da
        # print("Ist schon eins da")
        prev_mitglieder = PrevMitgliedAmt.objects.get(funktion=instance.funktion)
    else:
        # es ist keins da
        # print("Ist keins da")
        prev_mitglieder = PrevMitgliedAmt(funktion=instance.funktion)
        prev_mitglieder.save()

    # Hinzufügen des Entfernten mitglieds
    prev_mitglieder.members.clear()
    prev_mitglieder.members.add(instance.mitglied)
    # print(prev_mitglieder.members.all())
    pass

class PrevMitgliedAmt(models.Model):
    members = models.ManyToManyField(Mitglied)
    funktion = models.ForeignKey(Funktion, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()

class MitgliedMail(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.email + " " + self.mitglied.__str__()
