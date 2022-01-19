import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    # Arrange - This is the data each test will use unless we define alternative data in the test
    def setUp(self):
        self.drink = Drink("Red Wine", 4.50)
        self.pub = Pub("The Prancing Pony", 100.00, [self.drink])


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

