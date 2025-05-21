from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if price < 1.0 or price > 10.0:
            raise ValueError("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

