from django.test import TestCase, Client
from django.urls import reverse, resolve
import json

from mitglieder.models import Mitglied, MitgliedAmt, MitgliedMail

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.main_url = reverse('main')
        self.erstellen_url = reverse('erstellen')

    def test_main_GET(self):
        response = self.client.get(self.main_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mitglieder/mitglieder.html')

    def test_mitglied_erstellen_GET(self):
        response = self.client.get(self.erstellen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mitglieder/mitglied_erstellen_bearbeiten.html')
