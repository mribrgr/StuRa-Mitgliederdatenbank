from selenium import webdriver
from django.urls import reverse

def addMitglied(self):
    """
        Hinzufüghen eines Mitglieds mit default parametern

        :param self:
        :type self:
        :return: No return Value
        :rtype: None
    """
    # Suchen des Hinzufügen Buttons
    try:
        btnAddMitglied = self.browser.find_element_by_xpath("//a[@href='/mitglieder/erstellen']")
        #btnAddMitglied = self.browser.find_element_by_id('btn-mitadd')
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
        btnSave = self.browser.find_element_by_id('save_button')
    except:
        print("Es wurden nicht alle Objekte auf der Seite gefunden")

    # Einfügen der Form
    entVorname.send_keys('Hans')
    entNachname.send_keys('Peter')
    entSpitzname.send_keys('Hansi')

    # Referat auswählen
    self.browser.find_element_by_xpath("//input[@class='select-dropdown dropdown-trigger']").click()
    self.browser.find_element_by_xpath("//ul[@class='dropdown-content select-dropdown']/li[3]").click()

    # Bereich auswählen
    self.browser.find_element_by_xpath("//div[@id='div_selectbereich1']/div/div/input[@class='select-dropdown dropdown-trigger']").click()
    self.browser.find_element_by_xpath("//div[@id='div_selectbereich1']/div/div/ul[@class='dropdown-content select-dropdown']/li[3]").click()

    # Amt auswählen
    self.browser.find_element_by_xpath("//div[@id='div_selectamt1']/div/div/input[@class='select-dropdown dropdown-trigger']").click()
    self.browser.find_element_by_xpath("//div[@id='div_selectamt1']/div/div/ul[@class='dropdown-content select-dropdown']/li[3]").click()


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
    btnSave.click()

    # überprüfen ob alles geklapt hat
    self.assertEqual(self.browser.current_url,
                        self.live_server_url + reverse('mitglieder:homepage'),
                        msg="Weiterleitung nicht erfolgt")
    self.assertEqual(self.browser.find_element_by_xpath("//tr[@class='mitglied']/td[contains(text(), 'Hans Peter')]").text,
                        "Hans Peter",
                        msg="Hans Peter wurde nicht angelegt")
    pass
