import time

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin
from tests.MyFuncMitglieder import addMitglied

class TestMitgliedEntfernen(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_1MitgliedEntfernen_AsSuperuser(self):
        time.sleep(5)
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')


        time.sleep(5)
        """
            Login as Admin
        """
        loginAsLukasAdmin(self)
        addMitglied(self)

        """
            Löschen eines Mitglieds
        """
        self.browser.find_element_by_xpath("//form[@method='post']/label/span").click()
        self.browser.find_element_by_xpath("//a[@id='delbtnl']").click()
        self.browser.find_element_by_xpath("//a[@id='delmitgliederconfirm']").click()
        

        """
            Überprüfung ob Mitglied gelöscht
        """
        self.assertEqual(self.browser.find_element_by_xpath("//div[@id='notification']").text,
            "Mitglieder wurden erfolgreich gelöscht")

        pass
