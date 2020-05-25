from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from tests.MyFuncAemter import createAmt, createReferat, createUnterbereich
from django.urls import reverse

class TestAemtHinzufuegen(MyTestCase):
    """
        Hier wird getestet:

        * Ob ein Referat richtig über das AdminPanel Hinzugefügt wird
        * Ob ein Unterbereich richtig über das AdminPanel Hinzugefügt wird
        * Ob ein Amt richtig über das AdminPanel Hinzugefügt wird
        * Ein Komplextest ob man mit Hinzugefügten Referat/Unterbereich/Amt
        Ein neues Mitglied erstellen kann, und ob es in der Ämterübersicht übernommen wird
    """

    def test_1ReferatHinzufuegen_AsSuperuser(self):
        """
            Hier wird ein Referat hinzugefügt und überprüft ob es dann richtig
            übernommen wurde.
        """

        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat = "test_referat"
        createReferat(self, referat)
        pass

    def test_1UnterbereichHinzufuegen_AsSuperuser(self):
        """
            Hier wird ein Unterbereich hinzugefügt und überprüft ob es dann richtig
            übernommen wurde.
        """

        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        # Login as Admin + Navigation
        loginAsLukasAdmin(self)

        # Hinzufügen eines Unterbereichs
        referat = "Finanzen"
        unterbereich = "test_unterbereich"
        createUnterbereich(self, referat, unterbereich)
        pass

    def test_1AemtHinzufuegen_AsSuperuser(self):
        """
            Hier wird ein Amt hinzugefügt und überprüft ob es dann richtig
            übernommen wurde.
        """
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Amtes
        amt = "test_amt"
        referat = "Finanzen"
        unterbereich = "Buchhaltung"
        createAmt(self, referat, unterbereich, amt)
        pass

    def test_ReferatUnterbereichAmtHinzufuegen_AsSuperuser(self):
        """
            Dies ist ein Zusammenhängender Test
            Referat, Unterbereich und Amt werden neu angelegt.
            Ein neues Mitglied wird erstellt und diesem zugeordnet.
            Es wird Überprüft ob auch alles in die Ämterübersicht mitgenommen wird.
        """
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')


        # Login as Admin
        loginAsLukasAdmin(self)

        referat = "test_referat"
        unterbereich = "test_unterbereich"
        amt = "test_amt"

        """
            Erstellen von allen
        """
        createReferat(self, referat)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        createUnterbereich(self, referat, unterbereich)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        createAmt(self, referat, unterbereich, amt)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        """
            Hinzufügen eines Mitglieds mit den Parametern
        """
        # navigieren zu Mitglied hinzufügen
        self.browser.find_element_by_xpath("//a[@href='/mitglieder/erstellen']").click()

        # auswahl des Referates, Unterbereices, Amts
        self.browser.find_element_by_xpath("//div[@id='div_selectreferat1']/div/input").click()
        self.browser.find_element_by_xpath("//span[text()='%s']"%referat).click()

        self.browser.find_element_by_xpath("//div[@id='div_selectbereich1']/div/div/input").click()
        self.browser.find_element_by_xpath("//span[text()='%s']"%unterbereich).click()

        self.browser.find_element_by_xpath("//div[@id='div_selectamt1']/div/div/input").click()
        self.browser.find_element_by_xpath("//span[text()='%s']"%amt).click()

        # weitere Daten Hinzufügen
        self.browser.find_element_by_name('vorname').send_keys('Hans')
        self.browser.find_element_by_name('nachname').send_keys('Peter')
        self.browser.find_element_by_name('spitzname').send_keys('Hansi')
        self.browser.find_element_by_name('email1').send_keys('sxxxxx@htw-dresden.de')
        self.browser.find_element_by_name('strasse').send_keys('Straße der Freiheit')
        self.browser.find_element_by_name('hausnr').send_keys('24')
        self.browser.find_element_by_name('plz').send_keys('01561')
        self.browser.find_element_by_name('ort').send_keys('Ebersbach')
        self.browser.find_element_by_name('telefon_mobil').send_keys('0362594833')

        # Speichern
        self.browser.find_element_by_id('save_button').click()
        self.assertEqual(self.browser.current_url,
                            self.live_server_url + reverse('mitglieder:homepage'),
                            msg="Weiterleitung nicht erfolgt")
        self.assertEqual(self.browser.find_element_by_xpath("//tr[@class='mitglied']/td[contains(text(), 'Hans Peter')]").text,
                            "Hans Peter",
                            msg="Hans Peter wurde nicht angelegt")
        searchstring = amt + " " + unterbereich + " (Referat " + referat + ")"
        self.assertEqual(self.browser.find_element_by_xpath("//tr[@class='mitglied']/td/ul/li[contains(text(), '%s')]"%searchstring).text,
                            searchstring,
                            msg="Amt wurde nicht richtig zugewiesen")

        """
            Schauen in der Ämter Übersicht ob alles angezeigt wird
        """
        # navigieren zur Ämterübersicht
        self.browser.find_element_by_xpath("//a[@href='/aemter']").click()

        # öffnen der collabseables
        searchstring = "Referat " + referat
        self.browser.find_element_by_xpath("//div[text()='%s']"%searchstring).click()
        searchstring = "Bereich " + unterbereich
        self.browser.find_element_by_xpath("//div[text()='%s']"%searchstring).click()

        # überprüfen ob Amt da ist
        self.assertEqual(self.browser.find_element_by_xpath("//tr/td[contains(text(), '%s')]"%amt).text,
                            amt,
                            msg="Amt ist nicht in Übersicht Ämter vorhanden")
        """
        TODO: Schauen ob Person richtig einem Amt zugeordnet wurde
        self.assertEqual(self.browser.find_element_by_xpath("//tr/td[contains(text(), 'Hans Peter\n')]").text,
                            "Hans Peter",
                            msg="Hans Peter wurde nicht richtig dem Amt hinzugefügt")
        """
        pass
