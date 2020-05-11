from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time, _thread

"""
    Mit Namespace auf den link
    "{% url 'mitglieder:mitglieder_loeschen' %}"
"""

class TestMultiuser(StaticLiveServerTestCase):
    """This is a conceptual class representation of a simple BLE device (GATT Server). It is essentially an extended combination of the :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

    :param client: A handle to the :class:`simpleble.SimpleBleClient` client object that detected the device
    :type client: class:`simpleble.SimpleBleClient`
    :param addr: Device MAC address, defaults to None
    :type addr: str, optional
    :param addrType: Device address type - one of ADDR_TYPE_PUBLIC or ADDR_TYPE_RANDOM, defaults to ADDR_TYPE_PUBLIC
    :type addrType: str, optional
    :param iface: Bluetooth interface number (0 = /dev/hci0) used for the connection, defaults to 0
    :type iface: int, optional
    :param data: A list of tuples (adtype, description, value) containing the AD type code, human-readable description and value for all available advertising data items, defaults to None
    :type data: list, optional
    :param rssi: Received Signal Strength Indication for the last received broadcast from the device. This is an integer value measured in dB, where 0 dB is the maximum (theoretical) signal strength, and more negative numbers indicate a weaker signal, defaults to 0
    :type rssi: int, optional
    :param connectable: `True` if the device supports connections, and `False` otherwise (typically used for advertising ‘beacons’)., defaults to `False`
    :type connectable: bool, optional
    :param updateCount: Integer count of the number of advertising packets received from the device so far, defaults to 0
    :type updateCount: int, optional
    """

    # befor every test funktion
    def setUp(self):
        self.browsers = list()
        for i in range(0, 5):
            """
                hier muss der richtige Webtreiber ausgewählt werden
                1. Edge - Windows
                2. Firefox - Windows
                3. Firefox - Linux 
            """
            #browser = webdriver.Edge('tests\\edgedriver_win64\\msedgedriver.exe')
            browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-win64\\geckodriver.exe')
            #browser = webdriver.Firefox(executable_path='tests\\firefoxdriver-linux64\\geckodriver')
            self.browsers.append(browser)
            pass
        pass

    # after every test funktion
    def tearDown(self):
        try:
            for browser in self.browsers:
                browser.close()
        except:
            print('Error while closing')
        pass

    # Tests
    def test_foo(self):
        """Returns a list containing :class:`bluepy.btle.Characteristic` objects for the peripheral. If no arguments are given, will return all characteristics. If startHnd and/or endHnd are given, the list is restricted to characteristics whose handles are within the given range.

        :param startHnd: Start index, defaults to 1
        :type startHnd: int, optional
        :param endHnd: End index, defaults to 0xFFFF
        :type endHnd: int, optional
        :param uuids: a list of UUID strings, defaults to None
        :type uuids: list, optional
        :return: List of returned :class:`bluepy.btle.Characteristic` objects
        :rtype: list
        """
        for browser in self.browsers:
            try:
                browser.get(self.live_server_url)
            except:
                print('Error in opening login page')
            pass

        # Login
        for browser in self.browsers:
            try:
                btnLogin = browser.find_element_by_id('btn-login')
                btnLogin.click()
                pass
            except:
                print('Login Button not found')
                pass

        time.sleep(20)
        self.assertEquals(1, 1)
        pass