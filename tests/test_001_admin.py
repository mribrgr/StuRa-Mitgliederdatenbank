from tests.MyTestCase import MyTestCase
from tests.MyFuncLogin import loginAsLukasAdmin

class TestAdmin(MyTestCase):
    """
        Setup and Teardown Funktions are specified in
        MyTestCase
    """

    # Tests
    def test_login_superuser(self):
        """
            Hier wird getestet, ob man sich als Admin einloggen kann
        """
        # login
        loginAsLukasAdmin(self)

        """
            TODO: Check ob es ein Admin ist.
        """
        pass
