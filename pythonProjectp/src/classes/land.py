from src.classes.transport import Transport


class Land(Transport):

    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self.hasMotor = hasMotor

    def get_hasMotor(self):
        return self.hasMotor

    def display(self):
        print(self.name + " es un transporte de tierra que cuesta " + self.price + " . Tiene motor?: " + self.hasMotor)







