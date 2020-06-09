from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin
from tests.MyFuncMitglieder import addMitglied


class TestMitgliedEntfernen(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedEntfernen_AsSuperuser(self):
        # Login as Admin
        loginAsLukasAdmin(self)
        addMitglied(self)

        """
            Löschen eines Mitglieds
        """
        self.browser.find_element_by_xpath(
            "//form[@method='post']/label/span").click()
        self.browser.find_element_by_xpath("//a[@id='delbtnl']").click()
        self.browser.find_element_by_xpath(
            "//a[@id='delmitgliederconfirm']").click()

        """
            Überprüfung ob Mitglied gelöscht
        """
        text = self.browser.find_element_by_xpath("//div[@id='notification']")
        self.assertTrue(text)
        pass
