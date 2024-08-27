from abc import ABC, abstractclassmethod

class Vehicle(ABC):

    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("you drive the car")
    
    def stop(self):
        print("you stop the car")

# car = Car()
# car.go()
# car.stop()

class Boat(Vehicle):
    def go(self):
        print("you drive the boat")
    def stop(self):
        print("you stop the boat")

# boat = Boat()
# boat.stop()
# boat.go()