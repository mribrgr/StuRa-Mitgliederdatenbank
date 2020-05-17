import time

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from tests.MyFuncMitglieder import addMitglied

class TestMitgliedAendern(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedAendern_AsSuperuser(self):
        time.sleep(5)
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')


        time.sleep(5)
        """
            Login as Admin + Add an Mitglied
        """
        loginAsLukasAdmin(self)
        addMitglied(self)

        """
            Auswählen eines Mitglieds (Stift)
        """
        self.browser.find_element_by_xpath("//tbody/tr/td/a").click()

        """
            Verändern von Feldern
        """
        self.browser.find_element_by_xpath("//input[@id='vorname']").send_keys('_1')
        self.browser.find_element_by_xpath("//input[@id='nachname']").send_keys('_1')
        self.browser.find_element_by_xpath("//a[@id='save_button']").click()

        self.assertEqual(self.browser.find_element_by_xpath("//tr[@class='mitglied']/td[contains(text(), 'Hans_1 Peter_1')]").text,
                            "Hans_1 Peter_1",
                            msg="Hans Peter wurde nicht geändert")
        pass
