import time
from selenium import webdriver
from django.urls import reverse

from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin, loginAsLukasUser
from tests.MyFuncMitglieder import *


class TestMitgliedHinzufuegen(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedHinzufügen_AsSuperuser(self):
        """
            Hier wird getestet, ob man als Admin ein Mitglied Hinzufügen kann.
        """
        # Login as Admin
        loginAsLukasAdmin(self)
        addMitglied(self)
        pass

    def test_50MitgliederHinzufügen_AsSuperuser_lookAsUser(self):
        """
            Hier wird getestet, ob man als Admin 50 Mitglieder Hinzufügen kann und ob die Pagination Funktioniert.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        for value in range(25):
            # print(f"Mitglied {value} wird hinzugefügt")
            try:
                addMitgliedWithParameters(self,
                    f"Max_{value}", "Mustermann", "Musti")
                self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '1')]").click()
            except:
                # print(f"Mitglied {value} wurde übersprungen")
                pass
            pass

        # Test Mitglieder Pagination Seiten
        self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '1')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '2')]"))
        # self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '3')]"))
        # self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '4')]"))

        """
            Logout and login as User
        """
        self.browser.find_element_by_xpath("//li/a[@href='/logout']").click()
        loginAsLukasUser(self)

        # Test Mitglieder Pagination Seiten
        self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '1')]"))
        self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '2')]"))
        # self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '3')]"))
        # self.assertTrue(self.browser.find_element_by_xpath("//ul[@class='pagination']/li/a[contains(text(), '4')]"))
        pass
