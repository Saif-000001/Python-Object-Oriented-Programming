class Engine:
    def __init__(self, hores_power):
        self.hores_power = hores_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, hores_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(hores_power)
        self.wheel = [Wheel(wheel_size) for wheel in range(4)]
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.hores_power}(hp) {self.wheel[0].size}in"

car = Car(make='Ford', model='Mustaring', hores_power=500, wheel_size=18)

print(car.display_car())