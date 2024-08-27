# parents class
class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")

# Child class of Animal
class Dog(Animal):
    def speek(self):
        print('khew khew')

# Child class of Animal
class Cat(Animal):
    def speek(self):
        print('mew')

# Child class of Animal
class Mouse(Animal):
    def speek(self):
        print('chi chi')

dog = Dog('kutta')

cat = Cat('Chana')

mouse = Mouse('idure')

print(f"{dog.name} {dog.is_alive}")

print(f"{cat.name} {cat.is_alive}")

print(f"{mouse.name} {mouse.is_alive}")

print(dog.name)
dog.sleep()
dog.eat()
dog.speek()

print(mouse.name)
mouse.sleep()
mouse.eat()
mouse.speek()

print(cat.name)
cat.sleep()
cat.eat()
cat.speek()

