from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # print(f"the circle of area {3.14*self.radius*self.radius}cm^2")
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, base):
        self.base = base

    def area(self):
        # print(f"the square of area {self.base*self.base}cm^2")
        return self.base * self.base

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        # print(f"the triangle of area {self.base*self.height}cm^2")
        return self.base * self.height

class Pizza(Circle):
    def __init__(self, name, radius):
        super().__init__(radius)
        self.name = name
    

# circle = Circle(5)
# square = Square(3)
# triangle = Triangle(5,7)

# circle.area()
# square.area()
# circle.area()

shapes = [Circle(4), Square(3), Triangle(5,7), Pizza('pizza', 4)]

for shape in shapes:
    print(f"{shape.area()}cm^2")