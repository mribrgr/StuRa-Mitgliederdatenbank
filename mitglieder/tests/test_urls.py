from django.test import SimpleTestCase
from django.urls import reverse, resolve

from mitglieder.views import main_screen, mitgliedErstellenView, mitgliedBearbeitenView

class TestUrls(SimpleTestCase):
    def test_main_url_resolves(self):
        url = reverse('mitglieder:homepage')
        #print(resolve(url))
        self.assertEqual(resolve(url).func, main_screen)

    def test_erstellen_url_resolves(self):
        url = reverse('mitglieder:erstellenView')
        self.assertEqual(resolve(url).func, mitgliedErstellenView)

    """
    def test_bearbeiten_url_resolves(self):
        url = reverse('mitglieder:bearbeitenView')
        self.assertEquals(resolve(url).func, mitgliedBearbeitenView)#
    """
        