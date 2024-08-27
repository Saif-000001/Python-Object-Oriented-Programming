class Animal:
    alive = True

class Dog(Animal):
    def speek(self):
        print("Gaw Gaw")

class Cat(Animal):
    def speek(self):
        print('Meow!')

class Car:
    alive = False
    def speek(self):
        print('PIPPP')

animals = [Dog(), Cat(), Car()]

for animal in animals:
    print(animal.alive)
    animal.speek()