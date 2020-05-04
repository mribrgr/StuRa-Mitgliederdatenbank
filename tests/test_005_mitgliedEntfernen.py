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
            TODO: Löschen eines Mitglieds
        """

        checkbox = self.browser.find_element_by_xpath("//label[@for='chk-1']/span")
        checkbox.click()

        self.browser.find_element_by_xpath("//a[@id='delbtnl']").click()
        self.browser.find_element_by_xpath("//a[@id='delmitgliederconfirm']").click()

        time.sleep(120)
        pass