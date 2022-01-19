import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.havana = Drink("Havana 7", 4.00)
        self.peroni = Drink("Peroni", 5.00)