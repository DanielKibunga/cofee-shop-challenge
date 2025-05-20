class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = name

    def get_name(self):
        return self._name
