from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time, _thread

"""
    Mit Namespace auf den link
    "{% url 'mitglieder:mitglieder_loeschen' %}"
"""

class TestMultiuser(StaticLiveServerTestCase):

    # befor every test funktion
    def setUp(self):
        self.browsers = list()
        for i in range(0, 5):
            #browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
            browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-win64\\geckodriver.exe')
            self.browsers.append(browser)
            pass
        pass

    # after every test funktion
    def tearDown(self):
        try:
            for browser in self.browsers:
                browser.close()
        except:
            print('Error while closing')
        pass

    # Tests
    def test_foo(self):
        for browser in self.browsers:
            try:
                browser.get(self.live_server_url)
            except:
                print('Error in opening login page')
            pass

        # Login
        for browser in self.browsers:
            try:
                btnLogin = browser.find_element_by_id('btn-login')
                btnLogin.click()
                pass
            except:
                print('Login Button not found')
                pass

        time.sleep(20)
        self.assertEquals(1, 1)
        pass