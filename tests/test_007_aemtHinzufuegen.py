import time

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from selenium.webdriver.support.ui import Select

class TestAemtHinzufuegen(MyTestCase):
    """
        Hier wird getestet:
        * Ob ein Amt richtig über das AdminPanel Hinzugefügt wird
    """

    def test_1AemtHinzufuegen_AsSuperuser(self):
        """
            Hier wird ein Amt hinzugefügt und überprüft ob es dann richtig
            übernommen wurde.
        """
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')

        """
            Login as Admin + Navigation
        """
        loginAsLukasAdmin(self)

        # Navigieren zum Admin Pannel
        self.browser.find_element_by_xpath("//a[@href='/admin']").click()

        # Navigieren zu Amt Hinzufügen
        self.browser.find_element_by_xpath("//a[@href='/admin/aemter/amt/']").click()
        self.browser.find_element_by_xpath("//a[@href='/admin/aemter/amt/add/']").click()

        """
            Hinzufügen eines Amtes
        """
        amt = "test_amt"
        workload = "5"
        referat = "Finanzen"
        unterbereich = "Buchhaltung (Referat Finanzen)"

        #fill inputs
        self.browser.find_element_by_xpath("//input[@id='id_bezeichnung']").send_keys(amt)
        self.browser.find_element_by_xpath("//input[@id='id_workload']").send_keys(workload)

        #fill selects
        select_referat = Select(self.browser.find_element_by_xpath("//select[@id='id_referat']"))
        select_referat.select_by_visible_text(referat)

        select_unterbereich = Select(self.browser.find_element_by_xpath("//select[@id='id_unterbereich']"))
        select_unterbereich.select_by_visible_text(unterbereich)

        #summit form
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        """
            Überprüfung ob Amt hinzugefügt wurde
        """
        createt_amt = amt + " " + unterbereich
        self.assertTrue(self.browser.find_element_by_xpath("//a[contains(text(), '%s')]"%createt_amt))
        pass

    def test_1ReferatHinzufuegen_AsSuperuser(self):
        """
            Hier wird ein Referat hinzugefügt und überprüft ob es dann richtig
            übernommen wurde.
        """

        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')


        """
            Login as Admin + Navigation
        """
        loginAsLukasAdmin(self)

        # Navigieren zum Admin Pannel
        self.browser.find_element_by_xpath("//a[@href='/admin']").click()

        # Navigieren zu Referat Hinzufügen
        self.browser.find_element_by_xpath("//a[@href='/admin/aemter/referat/add/']").click()

        """
            Hinzufügen eines referat
        """
        referat = "test_referat"

        #fill inputs
        self.browser.find_element_by_xpath("//input[@id='id_bezeichnung']").send_keys(referat)

        #summit form
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        """
            Überprüfung ob Referat hinzugefügt wurde
        """
        self.assertTrue(self.browser.find_element_by_xpath("//a[contains(text(), '%s')]"%referat))
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


        """
            Login as Admin + Navigation
        """
        loginAsLukasAdmin(self)

        # Navigieren zum Admin Pannel
        self.browser.find_element_by_xpath("//a[@href='/admin']").click()

        # Navigieren zu Referat Hinzufügen
        self.browser.find_element_by_xpath("//a[@href='/admin/aemter/unterbereich/add/']").click()

        """
            Hinzufügen eines Unterbereichs
        """
        referat = "Finanzen"
        unterbereich = "test_unterbereich"

        #fill inputs
        self.browser.find_element_by_xpath("//input[@id='id_bezeichnung']").send_keys(unterbereich)

        #fill selects
        select_referat = Select(self.browser.find_element_by_xpath("//select[@id='id_referat']"))
        select_referat.select_by_visible_text(referat)

        #summit form
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        """
            Überprüfung ob Unterbereichs hinzugefügt wurde
        """
        createt_unterbereich = unterbereich + " (Referat " + referat + ")"
        self.assertTrue(self.browser.find_element_by_xpath("//a[contains(text(), '%s')]"%createt_unterbereich))
        pass
