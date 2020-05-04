import csv
from platform import system
from selenium import webdriver
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from aemter.models import Amt, Unterbereich, Referat


def loginAsLukasAdmin(self):
    # Suche aller Objekte der Seite
    try:
        entUsername = self.browser.find_element_by_id('id_username')
        entPassword = self.browser.find_element_by_id('id_password')
        btnLogin = self.browser.find_element_by_id('btn-login')
    except:
        print("Es wurden nicht alle Objekte auf der Seite gefunden")

    # Eingabe der Login-Daten
    entUsername.send_keys('testlukasadmin')
    entPassword.send_keys('0123456789test')
    btnLogin.click()

    # Check Login Success
    self.assertEqual(self.browser.current_url, self.live_server_url + reverse('mitglieder:homepage'), 
        msg="Konnte nicht angemeldet werden bzw. Weiterleitung nicht erfolgt")
    pass

def loginAsLukasUser(self):
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
    self.assertEqual(self.browser.current_url, self.live_server_url + reverse('mitglieder:homepage'), 
        msg="Konnte nicht angemeldet werden bzw. Weiterleitung nicht erfolgt")
    pass

class MyTestCase(StaticLiveServerTestCase):
    # befor every test funktion
    def setUp(self):
        """
            Auswahl des richtigen Webdriver anhand des Systemes
        """
        if system() == 'Windows':
            #self.browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
            self.browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-win64\\geckodriver.exe')
            pass
        if system() == 'Linux':
            self.browser = webdriver.Firefox(executable_path='tests/firefoxdriver-linux64/geckodriver')
            pass

        self.browser.implicitly_wait(10)

        """
            Hinzufügen von Admin
        """
        user = get_user_model().objects.create_superuser(username='testlukasadmin', password='0123456789test')

        """
            Hinzufügen von Nutzern
        """
        user = get_user_model().objects.create_user(username='testlukas', password='0123456789test')

        """
            Hinzufügen von Ämter - Kopiert von Theresa
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
                        #print("Referat " + referat + " gespeichert")
                        # Aemter
                        a = Amt(bezeichnung="Leitung", referat=r)
                        a.save()
                        a = Amt(bezeichnung="Stellvertretende Leitung", referat=r)
                        a.save()

                    else:
                        #print("Referat " + referat + " existiert bereits")
                        pass

        with open("bereiche.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                referat = row.pop(0)
                #print(referat)
                for bereich in row:
                    if Unterbereich.objects.filter(bezeichnung=bereich).exists()==False:
                        #print("Bereich " + bereich + " (Referat: " + referat + ") wird gespeichert")
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
        pass

    # after every test funktion
    def tearDown(self):
        try:
            #self.browser.close()
            self.browser.quit()
        except:
            print('Error while closing')
        pass
    pass
