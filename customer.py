class Customer:
    def __init__(self, name):
        self.set_name(name)
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    def add_order(self, order):
        self._orders.append(order)

    def get_orders(self):
        return self._orders

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.add_order(order)
        return order

