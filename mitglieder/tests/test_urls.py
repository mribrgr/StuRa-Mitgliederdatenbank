from django.test import SimpleTestCase
from django.urls import reverse, resolve

from mitglieder.views import main_screen, mitglied_bearbeiten, mitglied_erstellen

class TestUrls(SimpleTestCase):
    def test_main_url_resolves(self):
        url = reverse('main')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, main_screen)

    def test_erstellen_url_resolves(self):
        url = reverse('erstellen')
        self.assertEquals(resolve(url).func, mitglied_erstellen)

    def test_bearbeiten_url_resolves(self):
        url = reverse('bearbeiten')
        self.assertEquals(resolve(url).func, mitglied_bearbeiten)