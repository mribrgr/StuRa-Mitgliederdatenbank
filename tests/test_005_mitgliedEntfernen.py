import time

from tests.MyTestCase import MyTestCase, loginAsLukasAdmin

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
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')
        
        
        """
            Login as Admin
        """
        loginAsLukasAdmin(self)
        time.sleep(20)
        pass