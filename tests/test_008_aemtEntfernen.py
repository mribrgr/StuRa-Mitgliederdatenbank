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
            Hier wird ein Referat hinzugefügt um es dann wieder zu entfernen.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines referat
        referat = "test_referat"
        createReferat(self, referat)

        # Entfernen eines referat
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % referat).click()
        self.browser.find_element_by_xpath("//a[@class='deletelink']").click()
        self.browser.find_element_by_xpath(
            "//div/input[@type='submit']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        tmpbool = True
        try:
            self.browser.find_element_by_xpath(
                "//a[contains(text(), '%s')]" % referat)
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
        referat = "Finanzen"
        unterbereich = "test_unterbereich"
        createUnterbereich(self, referat, unterbereich)

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
            Hier wird ein Amt hinzugefügt um es dann wieder zu entfernen.
        """
        # Login as Admin
        loginAsLukasAdmin(self)

        # Hinzufügen eines Amtes
        amt = "test_amt"
        referat = "Finanzen"
        unterbereich = "Buchhaltung"
        createAmt(self, referat, unterbereich, amt)

        # Entfernen eines Amts
        self.browser.find_element_by_xpath(
            "//a[contains(text(), '%s')]" % amt).click()
        self.browser.find_element_by_xpath("//a[@class='deletelink']").click()
        self.browser.find_element_by_xpath(
            "//div/input[@type='submit']").click()

        # Überprüfen ob alles geklappt hat
        self.assertTrue(self.browser.find_element_by_xpath(
            "//li[@class='success']"))
        tmpbool = True
        try:
            self.browser.find_element_by_xpath(
                "//a[contains(text(), '%s')]" % amt)
        except BaseException:
            tmpbool = False
        self.assertFalse(tmpbool)
        pass
