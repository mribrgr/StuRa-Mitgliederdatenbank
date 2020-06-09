from django.test import TestCase
from mitglieder.models import *
from aemter.models import *

class TestModels(TestCase):

    def setUp(self):
        self.referat1 = Referat.objects.create(
            bezeichnung = "myreferat"
        )

        self.unterbereich1 = Unterbereich.objects.create(
            bezeichnung = "myunterbereich",
            referat = self.referat1
        )

        self.amt1 = Amt.objects.create(
            bezeichnung = "myamt1",
            workload = 4,
            referat = self.referat1,
            unterbereich = self.unterbereich1
        )

        self.amt2 = Amt.objects.create(
            bezeichnung = "myamt2",
            workload = 4,
            referat = self.referat1,
            unterbereich = None
        )

    def test_Referat_toString(self):
        self.assertEquals(
            self.referat1.__str__(),
            "myreferat")

    def test_Unterbereich_toString(self):
        self.assertEquals(
            self.unterbereich1.__str__(),
            "myunterbereich (Referat myreferat)")

    def test_Amt1_toString(self):
        self.assertEquals(
            self.amt1.__str__(),
            "myamt1 myunterbereich (Referat myreferat)")

    def test_Amt2_toString(self):
        self.assertEquals(
            self.amt2.__str__(),
            "myamt2 myreferat")
