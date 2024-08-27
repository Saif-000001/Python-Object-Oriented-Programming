class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def descirbe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'no filled'}")

class Circle(Shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def descirbe(self):
        super().descirbe()
        print(f'it is a circle with area of {3.14*self.radius*self.radius}cm^2')

class Triangle(Shape):

    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height
    
    def descirbe(self):
        super().descirbe()
        print(f'it is a triangle with area of {0.5*self.base*self.height}cm^2')

class Rectangle(Shape):
    
    def __init__(self, color, is_filled, Length, width):
        super().__init__(color, is_filled)
        self.Length = Length
        self.width = width
    
    def descirbe(self):
        super().descirbe()
        print(f'it is a rectangle with area of {self.Length*self.width}km^2')

circle = Circle('red', True, 3)
triangle = Triangle('blue', False, 7.8, 9)
rectangle = Rectangle('yellow', True, 7, 5)

triangle.descirbe()
rectangle.descirbe()
circle.descirbe()