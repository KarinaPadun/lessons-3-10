

class Car:
    def __init__(self, fuel, model, color):
        self.fuel = fuel
        self.model = model
        self.color = color

    def get_fuel(self):
        return f"This car uses {self.fuel}."

    def get_model(self):
        return f"This is a {self.model}."

    def get_color(self):
        return f"The car is {self.color}."



car = Car("Benz", "BMW", "red")


print(car.get_fuel())
print(car.get_model())
print(car.get_color())
