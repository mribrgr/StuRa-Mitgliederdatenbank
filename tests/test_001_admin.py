import time
from tests.MyTestCase import MyTestCase, loginAsLukasAdmin

class TestAdmin(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """
    
    # Tests
    def test_login_superuser(self):
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
        pass