import time
from selenium import webdriver
from django.urls import reverse

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from tests.MyFuncMitglieder import addMitglied

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
        addMitglied(self)
        pass