import time

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from tests.MyFuncAemter import createAmt, createReferat, createUnterbereich
from selenium.webdriver.support.ui import Select

class TestAemtHinzufuegen(MyTestCase):
    """
        Hier wird getestet:
        * Ob ein Amt richtig über das AdminPanel Hinzugefügt wird
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

        """
            TODO:
            Hier weiter machen
        """

        """
            TODO:
            Schauen in der Ämter Übersicht ob alles angezeigt wird
        """

        time.sleep(200)
        pass
