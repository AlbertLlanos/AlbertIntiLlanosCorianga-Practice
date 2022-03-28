from src.classes.transport import Transport
from src.classes.land import Land
from src.classes.bicycle import Bicycle
from src.classes.car import Car

if __name__ == "__main__":

    transport1: Transport = Transport("barco ", "50000")
    transport2: Transport = Land("Tractor", "55000", "True")
    transport3: Transport = Bicycle("MX montañera", "500", "False", "True")
    transport4: Transport = Car("Rav 4", "1000", "True", "False")

    transportList = [transport1, transport2, transport3, transport4]

    for transport in transportList:
        transport.display()