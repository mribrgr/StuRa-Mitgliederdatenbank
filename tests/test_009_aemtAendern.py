from selenium.webdriver.support.ui import Select
from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin
from tests.MyFuncAemter import createAmt, createReferat, createUnterbereich


class TestAemtAendern(MyTestCase):
    """
        Hier wird getestet:

        * Ob man alle Eigenschaften zu Referaten ändern kann
        * Ob man alle Eigenschaften zu Unterbereichen ändern kann
        * Ob man alle Eigenschaften zu Ämtern ändern kann

    """

    def test_1ReferatBezeichnungAendern(self):
        """
            Die Bezeichnung eines Referates wird geändert indem eine _1 angehängt wird
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat = "test_referat"
        createReferat(self, referat)

        # ändern der Bezeichnung für test_referat
        suffix = "_1"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % referat).click()
        self.browser.find_element_by_xpath(
            "//input[@id='id_bezeichnung']").send_keys(suffix)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % (referat + suffix)))
        pass

    def test_1UnterbereichBezeichnungAendern(self):
        """
            Die Bezeichnung eines Unterbereiches wird geändert indem eine _1 angehängt wird
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Unterbereichs
        referat = "Referat Finanzen"
        unterbereich = "test_unterbereich"
        createUnterbereich(self, referat, unterbereich)

        # ändern der Bezeichnung für test_unterbereich
        suffix = "_1"
        text = unterbereich + " (Organisationseinheit " + referat + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        self.browser.find_element_by_xpath(
            "//input[@id='id_bezeichnung']").send_keys(suffix)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        text = unterbereich + suffix + " (Organisationseinheit " + referat + ")"
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass

    def test_1UnterbereichReferatAendern(self):
        """
            Ändern des Referates, dem der Unterbereich zugeordnet ist
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat2 = "test_referat"
        createReferat(self, referat2)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        # Hinzufügen eines Unterbereichs
        referat = "Referat Finanzen"
        unterbereich = "test_unterbereich"
        createUnterbereich(self, referat, unterbereich)

        # ändern des Referates, dem der Bereich zugeordnet wurde
        text = unterbereich + " (Organisationseinheit " + referat + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        select_referat = Select(
            self.browser.find_element_by_xpath("//select[@id='id_referat']"))
        select_referat.select_by_visible_text(referat2)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        text = unterbereich + " (Organisationseinheit " + referat2 + ")"
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass

    def test_1AmtBezeichnungAendern(self):
        """
            Hier wird die Bezeichnung eines Amtes geändert indem eine _1 angehängt
            wird
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Amtes
        amt = "test_amt"
        referat = "Referat Finanzen"
        unterbereich = "Bereich Buchhaltung"
        createAmt(self, referat, unterbereich, amt)

        # ändern des Referates, dem der Bereich zugeordnet wurde
        suffix = "_1"
        text = amt + " " + unterbereich + " (Organisationseinheit " + referat + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        self.browser.find_element_by_xpath(
            "//input[@id='id_bezeichnung']").send_keys(suffix)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        text = amt + suffix + " " + unterbereich + " (Organisationseinheit " + referat + ")"
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass

    def test_1AmtWorkloadAendern(self):
        """
            Hier wird der Workload eines Amtes geändert
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Amtes
        amt = "test_amt"
        referat = "Referat Finanzen"
        unterbereich = "Bereich Buchhaltung"
        createAmt(self, referat, unterbereich, amt)

        # ändern des Referates, dem der Bereich zugeordnet wurde
        workload = "5"
        text = amt + " " + unterbereich + " (Organisationseinheit " + referat + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        self.browser.find_element_by_xpath(
            "//input[@id='id_workload']").send_keys(workload)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass

    def test_1AmtReferatAendern(self):
        """
            Hier wird das Organisationseinheit geändert, dem das Amt zugeordnet ist
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat2 = "test_referat"
        createReferat(self, referat2)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        # Hinzufügen eines Unterbereichs
        unterbereich2 = "test_unterbereich"
        createUnterbereich(self, referat2, unterbereich2)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        # Hinzufügen eines Amtes
        amt = "test_amt"
        referat = "Referat Finanzen"
        unterbereich = "Bereich Buchhaltung"
        createAmt(self, referat, unterbereich, amt)

        # ändern des Referates, dem der Bereich zugeordnet wurde
        workload = "5"
        text = amt + " " + unterbereich + " (Organisationseinheit " + referat + ")"
        text_ub = unterbereich2 + " (Organisationseinheit " + referat2 + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        select_referat = Select(
            self.browser.find_element_by_xpath("//select[@id='id_referat']"))
        select_referat.select_by_visible_text(referat2)
        select_unterbereich = Select(
            self.browser.find_element_by_xpath("//select[@id='id_unterbereich']"))
        select_unterbereich.select_by_visible_text(text_ub)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        text = amt + " " + unterbereich2 + " (Organisationseinheit " + referat2 + ")"
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass

    def test_1AmtUnterbereichAendern(self):
        """
            Hier wird der Unterbereich geändert, dem das Amt zugeordnet ist
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat = "test_referat"
        createReferat(self, referat)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        # Hinzufügen zwei Unterbereichs
        unterbereich = "test_unterbereich"
        createUnterbereich(self, referat, unterbereich)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        unterbereich2 = "test_unterbereich2"
        createUnterbereich(self, referat, unterbereich2)
        self.browser.find_element_by_xpath("//a[@href='/']").click()

        # Hinzufügen eines Amtes
        amt = "test_amt"
        createAmt(self, referat, unterbereich, amt)

        # ändern des Referates, dem der Bereich zugeordnet wurde
        workload = "5"
        text = amt + " " + unterbereich + " (Organisationseinheit " + referat + ")"
        text_ub = unterbereich2 + " (Organisationseinheit " + referat + ")"
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text).click()
        select_unterbereich = Select(
            self.browser.find_element_by_xpath("//select[@id='id_unterbereich']"))
        select_unterbereich.select_by_visible_text(text_ub)
        self.browser.find_element_by_xpath("//input[@name='_save']").click()

        # Überprüfen ob alles geklappt hat
        text = amt + " " + unterbereich2 + " (Organisationseinheit " + referat + ")"
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        self.assertTrue(self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % text))
        pass
