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
        """
            Öffnen der Website
        """
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
        # addMitglied(self) # bei einzelausführung kein Problem?
        # Fehler beim XPATH 

        """
            TODO: Löschen eines Mitglieds
        """

        #time.sleep(120)
        pass