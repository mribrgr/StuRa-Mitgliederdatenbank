from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from django.contrib.auth import get_user_model
from aemter.models import Amt, Unterbereich, Referat

import csv

class TestMitgliedHinzufuegen(StaticLiveServerTestCase):

    # befor every test funktion
    def setUp(self):
        """
            hier muss der richtige Webtreiber ausgewählt werden
            1. Edge - Windows
            2. Firefox - Windows
            3. Firefox - Linux 
        """
        #self.browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
        self.browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-win64\\geckodriver.exe')
        #self.browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-linux64\\geckodriver')
        pass

    # after every test funktion
    def tearDown(self):
        try:
            self.browser.close()
        except:
            print('Error while closing')
        pass

    # Tests
    def test_1MitgliedHinzufügen_AsSuperuser(self):
        user = get_user_model().objects.create_superuser(username='testlukas', password='0123456789test')

        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        # Suche aller Objekte der Seite
        try:
            entUsername = self.browser.find_element_by_id('id_username')
            entPassword = self.browser.find_element_by_id('id_password')
            btnLogin = self.browser.find_element_by_id('btn-login')
        except:
            print("Es wurden nicht alle Objekte auf der Seite gefunden")

        # Eingabe der Login-Daten
        entUsername.send_keys('testlukas')
        entPassword.send_keys('0123456789test')
        btnLogin.click()

        # Check Login Success
        self.assertEquals(self.browser.current_url, self.live_server_url + reverse('mitglieder:homepage'), 
            msg="Konnte nicht angemeldet werden bzw. Weiterleitung nicht erfolgt")

        """
            Kopiert von Theresa
        """
        Referat.objects.all().delete()
        Unterbereich.objects.all().delete()
        Amt.objects.all().delete()

        with open("referate.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                for referat in row:
                    if not Referat.objects.filter(bezeichnung=referat).exists():
                        r = Referat(bezeichnung=referat)
                        r.save()
                        print("Referat " + referat + " gespeichert")
                        # Aemter
                        a = Amt(bezeichnung="Leitung", referat=r)
                        a.save()
                        a = Amt(bezeichnung="Stellvertretende Leitung", referat=r)
                        a.save()

                    else:
                        print("Referat " + referat + " existiert bereits")

        with open("bereiche.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                referat = row.pop(0)
                print(referat)
                for bereich in row:
                    if Unterbereich.objects.filter(bezeichnung=bereich).exists()==False:
                        print("Bereich " + bereich + " (Referat: " + referat + ") wird gespeichert")
                        b = Unterbereich(bezeichnung=bereich, referat=Referat.objects.get(bezeichnung=referat))
                        b.save()
                        # Aemter
                        a = Amt(bezeichnung="Leitung", unterbereich=b, referat=b.referat)
                        a.save()
                        a = Amt(bezeichnung="Stellvertretende Leitung", unterbereich=b, referat=b.referat)
                        a.save()
                        a = Amt(bezeichnung="Beratendes Mitglied", unterbereich=b, referat=b.referat)
                        a.save()
        """
            Kopiert von Theresa
        """

        # Suchen des Hinzufügen Buttons
        try:
            btnAddMitglied = self.browser.find_element_by_id('btn-mitadd')
        except:
            print("Es wurden nicht alle Objekte auf der Seite gefunden")

        # Klicken des Buttons
        btnAddMitglied.click()

        # Suchen aller relevanten Objekte zum hinzufügen eines Mitglieds
        try:
            # Entrys
            entVorname = self.browser.find_element_by_name('vorname')
            entNachname = self.browser.find_element_by_name('nachname')
            entSpitzname = self.browser.find_element_by_name('spitzname')

            entStrasse = self.browser.find_element_by_name('strasse')
            entHausnr = self.browser.find_element_by_name('hausnr')
            entPlz = self.browser.find_element_by_name('plz')
            entOrt = self.browser.find_element_by_name('ort')
            entTelefon_mobil = self.browser.find_element_by_name('telefon_mobil')
            
            # Buttons
            btnAddEmail = self.browser.find_element_by_id('addEmailBtn')
            btnSave = self.browser.find_element_by_id('btn-save')
        except:
            print("Es wurden nicht alle Objekte auf der Seite gefunden")

        # Einfügen der Form
        entVorname.send_keys('Hans')
        entNachname.send_keys('Peter')
        entSpitzname.send_keys('Hansi')

        """
            TODO: Amt Hinzufügen
            TODO: Amt bzw. Referat auswählen
        """

        btnAddEmail.click()
        # Finden der Email Felder
        try:
            entEmail1 = self.browser.find_element_by_name('email1')
            entEmail2 = self.browser.find_element_by_name('email2')
        except:
            print("Es wurden nicht alle Objekte auf der Seite gefunden")

        # Eingabe der Emails
        entEmail1.send_keys('sxxxxx@htw-dresden.de')
        entEmail2.send_keys('Hans.Peter@web.de')

        # Einfügen der restlichen Daten der Form
        entStrasse.send_keys('Straße der Freiheit')
        entHausnr.send_keys('24')
        entPlz.send_keys('01561')
        entOrt.send_keys('Ebersbach')
        entTelefon_mobil.send_keys('0362594833')

        time.sleep(50)

        # Speichern der Daten
        #btnSave.click()
        pass