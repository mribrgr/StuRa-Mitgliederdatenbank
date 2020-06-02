from selenium import webdriver
from django.urls import reverse

from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin, loginAsLukasUser
from tests.MyFuncMitglieder import addMitglied


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

    def test_5MitgliederHinzufügen_AsSuperuser_lookAsUser(self):
        """
            Hier wird getestet, ob man als Admin 5 Mitglieder Hinzufügen kann.
        """
        # Login as Admin
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
        pass
