from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin
from tests.MyFuncAemter import createAmt, createReferat, createUnterbereich


class TestAemtEntfernen(MyTestCase):
    """
        Hier wird getestet:
        ...
    """

    def test_1ReferatEntfernen_AsSuperuser(self):
        """
            Hier wird ein Organisationseinheit hinzugefügt um es dann wieder zu entfernen.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines organisationseinheit
        organisationseinheit = "test_referat"
        createReferat(self, organisationseinheit)

        # Entfernen eines organisationseinheit
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % organisationseinheit).click()
        self.browser.find_element_by_xpath("//a[@class='deletelink']").click()
        self.browser.find_element_by_xpath(
            "//div/input[@type='submit']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        tmpbool = True
        try:
            self.browser.find_element_by_xpath(
                "//a[contains(text(), '%s')]" % organisationseinheit)
        except BaseException:
            tmpbool = False
        self.assertFalse(tmpbool)
        pass

    def test_1UnterbereichEntfernen_AsSuperuser(self):
        """
            Hier wird ein Unterbereich hinzugefügt um es dann wieder zu entfernen.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Unterbereichs
        organisationseinheit = "Referat Finanzen"
        unterbereich = "test_unterbereich"
        createUnterbereich(self, organisationseinheit, unterbereich)

        # Entfernen eines unterbereiches
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % unterbereich).click()
        self.browser.find_element_by_xpath("//a[@class='deletelink']").click()
        self.browser.find_element_by_xpath(
            "//div/input[@type='submit']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        tmpbool = True
        try:
            self.browser.find_element_by_xpath(
                "//a[contains(text(), '%s')]" % unterbereich)
        except BaseException:
            tmpbool = False
        self.assertFalse(tmpbool)
        pass

    def test_1AemtEntfernen_AsSuperuser(self):
        """
            Hier wird ein Funktion hinzugefügt um es dann wieder zu entfernen.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Amtes
        funktion = "test_amt"
        organisationseinheit = "Referat Finanzen"
        unterbereich = "Bereich Buchhaltung"
        createAmt(self, organisationseinheit, unterbereich, funktion)

        # Entfernen eines Amts
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % funktion).click()
        self.browser.find_element_by_xpath("//a[@class='deletelink']").click()
        self.browser.find_element_by_xpath(
            "//div/input[@type='submit']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        tmpbool = True
        try:
            self.browser.find_element_by_xpath(
                "//a[contains(text(), '%s')]" % funktion)
        except BaseException:
            tmpbool = False
        self.assertFalse(tmpbool)
        pass
