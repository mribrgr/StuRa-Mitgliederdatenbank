from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

from django.contrib.auth import get_user_model

"""
    Mit Namespace auf den link
    "{% url 'mitglieder:mitglieder_loeschen' %}"
"""

class TestAdmin(StaticLiveServerTestCase):

    # befor every test funktion
    def setUp(self):
        """
            hier muss der richtige Webtreiber ausgewählt werden
            1. Edge - Windows
            2. Firefox - Windows
            3. Firefox - Linux 
        """
        #self.browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
        self.browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-win64\\geckodriver.exe')
        #self.browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-linux64\\geckodriver')
        pass

    # after every test funktion
    def tearDown(self):
        try:
            self.browser.close()
        except:
            print('Error while closing')
        pass

    # Tests
    def test_foo(self):
        user = get_user_model().objects.create_user(username='testlukas', password='0123456789test')

        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

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
        self.assertEquals(self.browser.current_url, self.live_server_url + reverse('mitglieder:homepage'), 
            msg="Konnte nicht angemeldet werden bzw. Weiterleitung nicht erfolgt")
        pass