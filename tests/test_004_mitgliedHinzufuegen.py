import time
from selenium import webdriver
from django.urls import reverse

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin, loginAsLukasUser
from tests.MyFuncMitglieder import addMitglied

class TestMitgliedHinzufuegen(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedHinzufügen_AsSuperuser(self):
        time.sleep(5)
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        time.sleep(5)
        """
            Anmelden als Admin
        """
        loginAsLukasAdmin(self)
        addMitglied(self)
        pass

    def test_5MitgliederHinzufügen_AsSuperuser_lookAsUser(self):
        time.sleep(5)
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        time.sleep(5)
        """
            Anmelden als Admin
        """
        loginAsLukasAdmin(self)
        addMitglied(self)
        addMitglied(self)
        addMitglied(self)
        addMitglied(self)
        addMitglied(self)

        """
            Logout and login as User
        """
        self.browser.find_element_by_xpath("//li/a[@href='/logout']").click()
        loginAsLukasUser(self)
        time.sleep(10)
        pass
