class Transport:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def display(self):
        print(self. name + "es un transporte que cuesta " + self.price)