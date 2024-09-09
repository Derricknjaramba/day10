import unittest
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order
from coffee_shop.customer import Customer

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer = Customer("Alice")

    def test_num_orders(self):
        self.customer.create_order(self.coffee, 3.5)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        self.customer.create_order(self.coffee, 4.0)
        self.customer.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.average_price(), 5.0)

if __name__ == '__main__':
    unittest.main()
