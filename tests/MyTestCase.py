import csv
from platform import system
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from aemter.models import Amt, Unterbereich, Referat


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
        options.log.level = "trace"
        options.set_headless(headless=True)

        try:
            if system() == 'Windows':
                #self.browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
                self.browser = WebDriver(
                    timeout=10,
                    executable_path='tests/firefoxdriver-win64/geckodriver.exe',
                    firefox_options=options,
                    log_path='django.log',
                    keep_alive=False)
                pass
            if system() == 'Linux':
                self.browser = WebDriver(
                    timeout=10,
                    executable_path='tests/firefoxdriver-linux64/geckodriver',
                    firefox_options=options,
                    log_path='django.log',
                    keep_alive=False
                )
                pass

            self.browser.implicitly_wait(10)
        except BaseException:
            print("konnte keine Webdriver-Instanz bekommen")

        # Hinzufügen von Admin
        user = get_user_model().objects.create_superuser(
            username='testlukasadmin', password='0123456789test')

        # Hinzufügen von Nutzern
        user = get_user_model().objects.create_user(
            username='testlukas', password='0123456789test')

        """
            Hinzufügen von Ämter - Kopiert von Theresa
        """
        Referat.objects.all().delete()
        Unterbereich.objects.all().delete()
        Amt.objects.all().delete()

        with open("referate.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                for referat in row:
                    if not Referat.objects.filter(
                            bezeichnung=referat).exists():
                        r = Referat(bezeichnung=referat)
                        r.save()
                        #print("Referat " + referat + " gespeichert")
                        # Aemter
                        a = Amt(bezeichnung="Leitung", referat=r)
                        a.save()
                        a = Amt(
                            bezeichnung="Stellvertretende Leitung", referat=r)
                        a.save()

                    else:
                        #print("Referat " + referat + " existiert bereits")
                        pass

        with open("bereiche.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                referat = row.pop(0)
                # print(referat)
                for bereich in row:
                    if Unterbereich.objects.filter(
                            bezeichnung=bereich).exists() == False:
                        #print("Bereich " + bereich + " (Referat: " + referat + ") wird gespeichert")
                        b = Unterbereich(
                            bezeichnung=bereich,
                            referat=Referat.objects.get(
                                bezeichnung=referat))
                        b.save()
                        # Aemter
                        a = Amt(bezeichnung="Leitung",
                                unterbereich=b, referat=b.referat)
                        a.save()
                        a = Amt(bezeichnung="Stellvertretende Leitung",
                                unterbereich=b, referat=b.referat)
                        a.save()
                        a = Amt(bezeichnung="Beratendes Mitglied",
                                unterbereich=b, referat=b.referat)
                        a.save()
        """
            Kopiert von Theresa
        """
        pass

    # after every test funktion
    def tearDown(self):
        self.browser.quit()
    pass
