class Car:
    # Attributes
    def __init__(self, model, year, color, is_sale):
        self.mode = model
        self.year = year
        self.color = color
        self.is_sale = is_sale
    
    # Mathods
    def drive(self):
        print(f"You drive the {self.mode} {self.year} {self.color} {self.is_sale}")

    def stop(self):
        print(f"you stop the car {self.mode} {self.year} {self.color} {self.is_sale}")