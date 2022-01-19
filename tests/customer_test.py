from typing_extensions import Self
import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.adam = Customer("Adam", 50.2, 32)
        self.vodka = Drink("vodka", 3.50, 4)

    def test_customer_has_name(self):
        self.assertEqual("Adam", self.adam.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50.2, self.adam.wallet)

    def test_customer_balance_lower(self):
        self.adam.lower_wallet_balance(4)
        self.assertEqual(46.2, self.adam.wallet)

    def test_customer_has_age(self):
        self.assertEqual(32, self.adam.age)

    def test_customer_drunkenness(self):
        self.assertEqual(0, self.adam.drunkenness)
    
    def test_increase_drunkenness(self):
        self.adam.increase_drunkenness(self.vodka.alcohol_level)
        self.assertEqual(4, self.adam.drunkenness)