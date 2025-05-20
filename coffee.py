class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = name
        self._orders = []

    def get_name(self):
        return self._name

    def add_order(self, order):
        self._orders.append(order)

    def get_orders(self):
        return self._orders

    def get_customers(self):
        customers = []
        for order in self._orders:
            customer = order.get_customer()
            if customer not in customers:
                customers.append(customer)
        return customers
