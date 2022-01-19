import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.havana = Drink("Havana 7", 4.00, 2)
        self.peroni = Drink("Peroni", 5.00, 3)

    def test_drink_has_name(self):
        self.assertEqual("Havana 7", self.havana.name)
    
    def test_drink_has_price(self):
        self.assertEqual(4.00, self.havana.price)

    def test_drink_has_alchohol_level(self):
        self.assertEqual(2, self.havana.alcohol_level)