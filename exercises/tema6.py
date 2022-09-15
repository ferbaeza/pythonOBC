class Vehicle():
    color= None
    wheels= None
    doors= None

    def __init__(self, color, wheels, doors):
        print('This is Vehicle class, Car {} color with {} doors and {} wheels'.format(color,wheels,doors))

class Car(Vehicle):
    power= None
    speed= None

    def __init__(self, color, wheels, doors, power, speed):
        super().__init__(color, wheels, doors)
        print('Car Class from Vehicle Class with {} cv and run up to {} km/h'.format(power, speed))

toyota=Car('white',4,4,125, 220)