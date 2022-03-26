from src.classes.land import Land

class Car(Land):

    def __init__(self, name, price, hasMotor, useGas):
        super().__init__(name, price, hasMotor)
        self.useGas = useGas

    def get_useGas(self):
        return self.useGas

    def display(self):
        print(self.name + " es un auto que cuesta " + self.price + ". Tiene motor?: " + self.hasMotor + ". Usa gas?:" + self.useGas)
