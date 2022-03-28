from src.classes.land import Land

class Bicycle(Land):

    def __init__(self, name, price, hasMotor, exerciseBike):
        super().__init__(name, price, hasMotor)
        self.exerciseBike = exerciseBike

    def get_exerciseBike(self):
        return self.exerciseBike

    def display(self):
        print(self.name + " es una bicicleta que cuesta " + self.price + ". Tiene motor?: " + self.hasMotor + ". Es una bicicleta de ejercicio?:" + self.exerciseBike)