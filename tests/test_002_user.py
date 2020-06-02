from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasUser


class TestUser(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_login_user(self):
        """
            Hier wird getestet, ob man sich als User anmelden kann.
        """
        # Login as User
        loginAsLukasUser(self)

        """
            TODO: Check ob es ein User ist.
        """
        pass
