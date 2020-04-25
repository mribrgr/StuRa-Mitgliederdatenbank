import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from django.urls import reverse

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin

class TestMitgliedHinzufuegen(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedHinzufügen_AsSuperuser(self):
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        """
            Anmelden als Admin
        """
        loginAsLukasAdmin(self)

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
            TODO: Amt bzw. Referat auswählen
        """
        self.browser.find_element_by_xpath("//input[@class='select-dropdown dropdown-trigger']").click()
        self.browser.find_element_by_xpath("//ul[@class='dropdown-content select-dropdown']/li[2]").click()
        time.sleep(120)
        

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

        # Speichern der Daten
        #btnSave.click()
        time.sleep(120)
        pass