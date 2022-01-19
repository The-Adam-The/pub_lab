from typing_extensions import Self
import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.adam = Customer("Adam", 50.2)

    def test_customer_has_name(self):
        self.assertEqual("Adam", self.adam.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50.2, self.adam.wallet)

    def test_customer_balance_lower(self):
        self.adam.lower_wallet_balance(4)
        self.assertEqual(46.2, self.adam.wallet)