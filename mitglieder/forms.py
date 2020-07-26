from django import forms
from mitglieder.models import Mitglied, MitgliedAmt, MitgliedMail
from aemter.models import Funktion, Unterbereich, Organisationseinheit

class MitgliedForm(forms.Form):
    vorname = forms.CharField(required=True)
    name = forms.CharField(required=True, label='nachname')
    spitzname = forms.CharField(required=False)
    strasse = forms.CharField(required=False)
    hausnr = forms.CharField(required=False)
    plz = forms.CharField(required=False)
    ort = forms.CharField(required=False)
    tel_mobil = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mitgliedaemter = MitgliedAmt.objects.filter(mitglied=self.get_object())
        for i in range(len(mitgliedaemter) + 1):
            field_names = ['organisationseinheit_%s' % (i,), 'unterbereich_%s' % (i,), 'referat_%s' % (i,)]
            for name in field_names:
                self.field[name] = forms.IntegerField(required=True)
            try:
                self.initial[field_names[0]] = mitgliedaemter[i].funktion.organisationseinheit.id
            except IndexError:
                self.initial[field_names[0]] = ""
            try:
                self.initial[field_names[1]] = mitgliedaemter[i].funktion.unterbereich.id
            except IndexError:
                self.initial[field_names[1]] = "-1"
            try:
                self.initial[field_names[2]] = mitgliedaemter[i].funktion.id
            except IndexError:
                self.initial[field_names[2]] = ""


    # def clean(self):
    
    def save(self):
        mitglied = self.instance
        mitglied.name = self.cleaned_data['nachname']
        mitglied.vorname = self.cleaned_data['vorname']

        mitglied.mitgliedamt_set.all().delete()

            