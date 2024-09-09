import unittest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Doe")
        self.coffee = Coffee("Espresso")

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIn(order, self.customer.orders())
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        other_customer = Customer("Jane Doe")
        other_customer.create_order(self.coffee, 6.0)
        aficionado = Customer.most_aficionado(self.coffee)
        self.assertEqual(aficionado, other_customer)

if __name__ == '__main__':
    unittest.main()
