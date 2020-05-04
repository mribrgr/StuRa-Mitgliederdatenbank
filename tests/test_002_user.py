import time
from tests.MyTestCase import MyTestCase, loginAsLukasUser

class TestUser(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """
    
    # Tests
    def test_login_user(self):
        time.sleep(5)
        try:
            self.browser.get(self.live_server_url)
        except:
            print('Error in opening login page')
        
        time.sleep(5)
        """
            Login as User
        """
        loginAsLukasUser(self)

        """
            TODO: Check ob es ein User ist.
        """
        pass