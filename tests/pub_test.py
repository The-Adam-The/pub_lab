import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    # Arrange - This is the data each test will use unless we define alternative data in the test
    def setUp(self):
        self.drink = Drink("Red Wine", 4.50, 3)
        self.pub = Pub("The Prancing Pony", 100.00, [self.drink])
        self.steph = Customer("Steph", 20, 34)
        self.billy = Customer("Billy", 16, 16)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        # Arrange - see above
        # Act
        self.pub.increase_till(2.50)
        # Assert
        self.assertEqual(102.50, self.pub.till)

    def test_pub_has_list_of_drinks(self):
        self.assertEqual([self.drink],self.pub.drink_list)


    def test_customer_legal_age(self):
        self.assertEqual(True, self.pub.customer_legal_age(self.steph.age) )

    def test_customer_not_legal_age(self):
        self.assertEqual(False, self.pub.customer_legal_age(self.billy.age) )  

    def test_purchase_drink(self):
        self.pub.purchase_drink(self.drink, self.steph)
        self.assertEqual(104.5, self.pub.till)
        self.assertEqual(15.5, self.steph.wallet)
        self.assertEqual(3, self.steph.drunkenness)

    def test_purchase_drink_underage(self):
        self.pub.purchase_drink(self.drink, self.billy)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(16, self.billy.wallet)

    def test_alchohol_serving_limit(self):
        self.assertEqual(15, self.pub.alchohol_limit_)


    def test_decline_service_not_drunk(self):
        self.assertEqual(False, self.pub.decline_service_too_drunk(self.steph.drunkenness, self.pub.alchohol_limit_))