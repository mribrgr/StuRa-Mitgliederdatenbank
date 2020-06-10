import csv
from platform import system
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from aemter.models import Amt, Unterbereich, Organisationseinheit
import importscripts.main as imp


class MyTestCase(StaticLiveServerTestCase):
    """
        Setup and Teardown funktions are specified here.

    """
    # befor every test funktion

    def setUp(self):
        """
            Auswahl des richtigen Webdriver anhand des Systemes
        """
        # Auskommentieren bei localen tests
        options = Options()
        #options.log.level = "trace"
        #options.headless = True

        try:
            if system() == 'Windows':
                #self.browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
                self.browser = WebDriver(
                    timeout=5,
                    executable_path='tests/firefoxdriver-win64/geckodriver.exe',
                    firefox_options=options,
                    log_path='django.log',
                    keep_alive=True)
                pass
            if system() == 'Linux':
                self.browser = WebDriver()
                # timeout=5,
                # executable_path='tests/firefoxdriver-linux64/geckodriver',
                # firefox_options=options,
                # log_path='django.log',
                # keep_alive=True
                pass

            self.browser.implicitly_wait(5)
            # self.browser.fullscreen_window()
        except BaseException as e:
            print("konnte keine Webdriver-Instanz bekommen")
            print(e)

        # Hinzufügen von Admin
        user = get_user_model().objects.create_superuser(
            username='testlukasadmin', password='0123456789test')

        # Hinzufügen von Nutzern
        user = get_user_model().objects.create_user(
            username='testlukas', password='0123456789test')

        # Hinzufügen von Ämter - über Importscript
        file = open("importscripts/ReferateUnterbereicheAemter.csv", encoding="utf-8")
        imp.importAemter(file)
        pass

    # after every test funktion
    def tearDown(self):
        self.browser.quit()
    pass
