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
        unterbereich = "Buchhaltung (Referat Finanzen)"
        createAmt(self, referat, unterbereich, amt)
        pass
