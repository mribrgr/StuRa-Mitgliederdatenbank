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
    amtszeit_beginn = models.DateField(null=True)
    amtszeit_ende = models.DateField(null=True)
    amtszeit_count = models.IntegerField(null=False, default=0)
    history = HistoricalRecords()
    def __str__(self):
        return self.mitglied.__str__() + ", " + self.funktion.__str__()

"""
@receiver(post_delete, sender=MitgliedAmt)
def delete_MitgliedAmt_hook(sender, instance, using, **kwargs):
    print("post_delete")
    mitglieder_count = PrevMitgliedAmt.objects.filter(funktion=instance.funktion).count()
    # Überprüfen ob schon eine PrevMitgliedAmt Liste für die funktion da ist
    if mitglieder_count != 0:
        # es ist schon eins da
        # print("Ist schon eins da")
        prev_mitglieder = PrevMitgliedAmt.objects.get(funktion=instance.funktion)
    else:
        # es ist keins da
        # print("Ist keins da")
        prev_mitglieder = PrevMitgliedAmt(funktion=instance.funktion)
        prev_mitglieder.save()

    # Anzahl der Mitglieder in der Liste ermitteln
    prev_mitglieder_count = prev_mitglieder.members.count()
    # wenn zwei Mitglieder in der Liste sind, das aelteste entfernen
    if prev_mitglieder_count == 2:
        prev_mitglieder.members.order_by('nummer')[0].delete()

    if prev_mitglieder_count != 0:
        mitgliedschaft_nummer = prev_mitglieder.members.order_by('-nummer')[0].nummer + 1
    else:
        mitgliedschaft_nummer = 1

    # Hinzufügen des Entfernten mitglieds
    mitglied_nummer_paar = MitgliedNummerPaar(mitglied=instance.mitglied,nummer=mitgliedschaft_nummer)
    mitglied_nummer_paar.save()
    prev_mitglieder.members.add(mitglied_nummer_paar)
    print(prev_mitglieder.members.all())
    pass

    # Mitglied und Nummer, die beschreibt, die wie vielte Kandidatur dieser Funktion das Mitglied ausgeuebt hat
class MitgliedNummerPaar(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    nummer = models.IntegerField(null=False)
    def __str__(self):
        return "Mitglied Nr. " + str(self.nummer) + ": " + self.mitglied.__str__() 


class PrevMitgliedAmt(models.Model):
    # Liste mit allen Instanzen MitgliedAmt der zugehörigen Funktion
    members = models.ManyToManyField(MitgliedNummerPaar)
    funktion = models.ForeignKey(Funktion, on_delete=models.CASCADE, null=False)
    history = HistoricalRecords()
"""

class MitgliedMail(models.Model):
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()
    def __str__(self):
        return self.email + " " + self.mitglied.__str__()