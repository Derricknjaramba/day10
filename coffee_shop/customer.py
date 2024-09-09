class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = new_name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not cls.all_customers:
            return None
        customer_expenses = {}
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > 0:
                customer_expenses[customer] = total_spent
        return max(customer_expenses, key=customer_expenses.get, default=None)
